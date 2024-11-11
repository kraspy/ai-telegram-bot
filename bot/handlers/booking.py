from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from datetime import date as d

from bot.states.states import BookingStates
from bot.keyboards.inline_keyboards import (
    dates_keyboard,
    times_keyboard,
    confirmation_keyboard,
    main_menu_keyboard,
)
from bot import messages

from database.database import Database

from yclients import YClients
from yclients.services.online_bookings_service.models import (
    BookableDatesQueryParams,
    BookableDatesRequest,
    BookableTimesQueryParams,
    BookableTimesRequest,
    BookRecordRequestBody,
    BookRecordRequest,
)
from yclients.services.online_bookings_service.models._additional import Appointment
from yclients.services.services_service.models import (
    ServicesRequestQueryParams,
    ServicesRequest,
    ServicesResponse,
)

router = Router()
STAFF_ID = 3353649


@router.callback_query(
    BookingStates.choosing_date,
    F.data.startswith('book_service_'),
)
async def choose_service(
    callback_query: types.CallbackQuery,
    state: FSMContext,
    yclients: YClients,
):
    '''Обрабатывает выбор услуги и предлагает пользователю выбрать дату.

    Args:
        callback_query (types.CallbackQuery): Callback запрос от пользователя.
        state (FSMContext): Контекст состояния FSM.
    '''
    service_id = int(callback_query.data.removeprefix('book_service_'))  # type: ignore
    await state.update_data(selected_service_id=service_id)

    request_model = BookableDatesRequest(
        query=BookableDatesQueryParams(service_ids=[service_id]),
    )

    dates_response = await yclients.online_bookings.get_bookable_dates(request_model=request_model)
    if dates_response and dates_response.success:
        dates = dates_response.data.booking_dates
        if dates:
            await callback_query.message.edit_text(  # type: ignore
                messages.CHOOSE_DATE,
                reply_markup=dates_keyboard(dates),
            )
            await state.set_state(BookingStates.choosing_date)
        else:
            await callback_query.message.edit_text(  # type: ignore
                messages.NOT_AVAILABLE_DATES,
            )
            await state.clear()
    else:
        await callback_query.message.edit_text(  # type: ignore
            messages.ERROR_GETTING_DATES,
        )
    await callback_query.answer()


@router.callback_query(
    BookingStates.choosing_date,
    F.data.startswith('date_'),
)
async def choose_date(
    callback_query: types.CallbackQuery,
    state: FSMContext,
    yclients: YClients,
):
    '''Обрабатывает выбор даты и предлагает пользователю выбрать время.

    Args:
        callback_query (types.CallbackQuery): Callback запрос от пользователя.
        state (FSMContext): Контекст состояния FSM.
        yclients (YClients): Экземпляр клиента API YClients.
    '''
    date_str = callback_query.data.removeprefix('date_')  # type: ignore
    date = d.fromisoformat(date_str)
    await state.update_data(selected_date=date)
    data = await state.get_data()
    service_id = data.get('selected_service_id')

    request_model = BookableTimesRequest(
        query=BookableTimesQueryParams(service_ids=[service_id]),  # type: ignore
    )

    times_response = await yclients.online_bookings.get_bookable_times(
        staff_id=STAFF_ID,
        date=date,
        request_model=request_model,  # type: ignore
    )
    if times_response and times_response.success:
        times = times_response.data
        if times:
            keyboard = times_keyboard(times)
            await callback_query.message.edit_text(  # type: ignore
                messages.CHOOSE_TIME,
                reply_markup=keyboard,
            )
            await state.set_state(BookingStates.choosing_time)
        else:
            await callback_query.message.edit_text(  # type: ignore
                messages.NOT_AVAILABLE_TIMES,
            )
            await state.clear()
    else:
        await callback_query.message.edit_text(  # type: ignore
            messages.ERROR_GETTING_TIMES,
        )
    await callback_query.answer()


@router.callback_query(
    BookingStates.choosing_time,
    F.data.startswith('time_'),
)
async def choose_time(
    callback_query: types.CallbackQuery,
    state: FSMContext,
    yclients: YClients,
):
    '''Обрабатывает выбор времени и запрашивает подтверждение у пользователя.

    Args:
        callback_query (types.CallbackQuery): Callback запрос от пользователя.
        state (FSMContext): Контекст состояния FSM.
        yclients (YClients): Экземпляр клиента API YClients.
    '''
    time = callback_query.data.removeprefix('time_')  # type: ignore
    await state.update_data(selected_time=time)
    data = await state.get_data()

    request_model = ServicesRequest(
        query=ServicesRequestQueryParams(),
    )

    response: ServicesResponse = await yclients.services.get_services(
        request_model=request_model,
        service_id=data.get('selected_service_id'),
    )
    service_name = response.data['booking_title']  # type: ignore

    await callback_query.message.edit_text(  # type: ignore
        messages.CONFIRMATION_TEXT.format(
            service_name=service_name,
            date=data.get('selected_date'),
            time=data.get('selected_time'),
        ),
        reply_markup=confirmation_keyboard(),
    )
    await state.set_state(BookingStates.confirming)
    await callback_query.answer()


@router.callback_query(
    BookingStates.confirming,
    F.data == 'confirm_yes',
)
async def confirm_booking_yes(
    callback_query: types.CallbackQuery,
    state: FSMContext,
    yclients: YClients,
    db: Database,
):
    '''Обрабатывает подтверждение бронирования и создает запись.

    Args:
        callback_query (types.CallbackQuery): Callback запрос от пользователя.
        state (FSMContext): Контекст состояния FSM.
        yclients (YClients): Экземпляр клиента API YClients.
        db (Database): Экземпляр базы данных.
    '''
    data = await state.get_data()
    user_data = await db.get_user_by_telegram_id(callback_query.from_user.id)

    service_response = await yclients.services.get_services(
        ServicesRequest(query=ServicesRequestQueryParams()),
        service_id=data.get('selected_service_id'),
    )
    service_name = service_response.data['booking_title']  # type: ignore

    if user_data:
        appointment = Appointment(
            id=1,
            services=[data['selected_service_id']],
            staff_id=STAFF_ID,
            datetime=f'{data['selected_date']}T{data['selected_time']}:00',  # type: ignore
        )
        booking_request = BookRecordRequest(
            body=BookRecordRequestBody(
                phone=user_data['phone'],
                fullname=f'{user_data['surname']} {user_data['name']} {user_data['patronymic']}',
                email='',
                appointments=[appointment],
            ),
        )  # type: ignore

        booking_response = await yclients.online_bookings.create_book_record(booking_request)
        if booking_response and booking_response.success:
            await callback_query.message.edit_text(  # type: ignore
                messages.BOOKING_SUCCESS.format(
                    service_name=service_name,
                    date=data.get('selected_date'),
                    time=data.get('selected_time'),
                )
            )
            await state.clear()
        else:
            await callback_query.message.edit_text(  # type: ignore
                messages.BOOK_NOT_CREATED,
            )
            await state.clear()
    else:
        await callback_query.message.edit_text(  # type: ignore
            messages.USER_NOT_FOUND,
        )
        await state.clear()
    await callback_query.answer()


@router.callback_query(
    BookingStates.confirming,
    F.data == 'confirm_no',
)
async def confirm_booking_no(
    callback_query: types.CallbackQuery,
    state: FSMContext,
):
    '''Обрабатывает отказ от бронирования пользователем.

    Args:
        callback_query (types.CallbackQuery): Callback запрос от пользователя.
        state (FSMContext): Контекст состояния FSM.
    '''
    await callback_query.message.edit_text(  # type: ignore
        messages.BOOKING_CANCELLED,
        reply_markup=main_menu_keyboard(),
    )
    await state.clear()
    await callback_query.answer()


@router.callback_query(
    BookingStates.confirming,
)
async def confirm_booking_invalid(
    callback_query: types.CallbackQuery,
    state: FSMContext,
):
    '''Обрабатывает некорректные команды во время подтверждения бронирования.

    Args:
        callback_query (types.CallbackQuery): Callback запрос от пользователя.
        state (FSMContext): Контекст состояния FSM.
    '''
    await callback_query.message.edit_text(  # type: ignore
        messages.UNKNOWN_COMMAND,
        reply_markup=main_menu_keyboard(),
    )
    await state.clear()
    await callback_query.answer()


def register_booking_handlers(dp):
    '''Регистрирует обработчики, связанные с бронированием.

    Args:
        dp: Диспетчер для регистрации обработчиков.
    '''
    dp.include_router(router)
