from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from bot import messages
from bot.keyboards.inline_keyboards import (
    services_keyboard,
    make_an_appointment_keyboard,
)
from bot.states.states import ServiceDescriptionStates, BookingStates

from yclients import YClients
from yclients.utils import get_manager
from yclients.services.online_bookings_service import OnlineBookingsService
from yclients.services.online_bookings_service.models import (
    BookableServicesQueryParams,
    BookableServicesRequest,
)

router = Router()


@router.callback_query(F.data == 'menu_services')
async def send_services_list(
    callback_query: types.CallbackQuery,
    state: FSMContext,
    yclients: YClients,
):
    '''Отправляет список доступных услуг пользователю.

    Args:
        callback_query (types.CallbackQuery): Callback-запрос от пользователя.
        state (FSMContext): Контекст состояния FSM.
        yclients (YClients): Клиент API YClients.
    '''
    service = OnlineBookingsService(get_manager())

    request_model = BookableServicesRequest(
        query=BookableServicesQueryParams(),
    )

    services_response = await service.get_bookable_services(request_model=request_model)

    if services_response and services_response.success:
        services = services_response.data.services

        await callback_query.message.edit_text(  # type: ignore
            text=messages.SELECT_SERVICE,
            reply_markup=services_keyboard(services),
        )

        await state.set_state(ServiceDescriptionStates.choosing_service_description)

    else:
        await callback_query.message.edit_text(  # type: ignore
            messages.SERVICES_UNAVAILABLE,
        )
    await callback_query.answer()


@router.callback_query(
    ServiceDescriptionStates.choosing_service_description,
    F.data.startswith('service_'),
)
async def service_description(
    callback_query: types.CallbackQuery,
    state: FSMContext,
    yclients: YClients,
):
    '''Отображает описание выбранной услуги и предлагает записаться.

    Args:
        callback_query (types.CallbackQuery): Callback-запрос от пользователя.
        state (FSMContext): Контекст состояния FSM.
        yclients (YClients): Клиент API YClients.
    '''
    service_id = int(callback_query.data.removeprefix('service_'))  # type: ignore

    service_description = messages.SERVICE_DESCRIPTIONS.get(service_id)

    if service_description is None:
        return

    await callback_query.message.edit_text(  # type: ignore
        text=service_description,
        reply_markup=make_an_appointment_keyboard(service_id=service_id),
    )
    await state.update_data(selected_service_id=service_id)
    await state.set_state(BookingStates.choosing_date)
    await callback_query.answer()


def register_services_handlers(dp):
    '''Регистрирует обработчики услуг в диспетчере.

    Args:
        dp: Диспетчер для регистрации обработчиков.
    '''
    dp.include_router(router)
