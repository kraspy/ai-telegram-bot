from aiogram import Dispatcher, Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram.types import ReplyKeyboardRemove

from bot import messages
from bot.keyboards.inline_keyboards import (
    cancel_registration_keyboard,
    main_menu_keyboard,
)
from bot.keyboards.keyboards import share_contact_keyboard
from bot.states.states import RegistrationStates
from bot.utils.validation import validate_fullname, validate_phone

from database import Database

from yclients import YClients
from yclients.services.clients_service.models import (
    CreateClientsRequestBody,
    CreateClientRequest,
)

router = Router()


@router.callback_query(F.data == 'registration_again')
async def start_registration(
    message: types.Message,
    state: FSMContext,
):
    '''Запускает процесс регистрации пользователя.

    Args:
        message (types.Message): Сообщение от пользователя.
        state (FSMContext): Контекст состояния FSM.
    '''
    await message.answer(
        messages.REGISTRATION_SHARE_CONTACT,
        reply_markup=share_contact_keyboard(),
    )
    await state.set_state(RegistrationStates.waiting_for_contact)


@router.message(RegistrationStates.waiting_for_contact, F.contact)
async def process_contact(
    message: types.Message,
    state: FSMContext,
):
    '''Обрабатывает получение контакта пользователя.

    Args:
        message (types.Message): Сообщение от пользователя.
        state (FSMContext): Контекст состояния FSM.
    '''
    contact = message.contact

    if contact.user_id != message.from_user.id:  # type: ignore
        await message.answer(
            messages.INVALID_SHARED_CONTACT,
            reply_markup=share_contact_keyboard(),
        )
        return

    phone = validate_phone(contact.phone_number)  # type: ignore
    if not phone:
        await message.answer(
            messages.INVALID_SHARED_CONTACT,
            reply_markup=share_contact_keyboard(),
        )
        return

    await state.update_data(phone=phone)
    await message.answer(
        messages.REGISTRATION_ENTER_NAME,
        reply_markup=ReplyKeyboardRemove(),
    )
    await state.set_state(RegistrationStates.waiting_for_fullname)


@router.message(RegistrationStates.waiting_for_contact)
async def invalid_contact(message: types.Message):
    '''Отправляет сообщение об ошибке при некорректном контакте.

    Args:
        message (types.Message): Сообщение от пользователя.
    '''
    await message.answer(
        messages.INVALID_DATA_SHARED_CONTACT,
        reply_markup=cancel_registration_keyboard(),
    )


@router.message(RegistrationStates.waiting_for_fullname, F.text)
async def process_fullname(
    message: types.Message,
    state: FSMContext,
    db: Database,
    yclients: YClients,
):
    '''Обрабатывает ввод полного имени пользователя.

    Args:
        message (types.Message): Сообщение от пользователя.
        state (FSMContext): Контекст состояния FSM.
        db (Database): Экземпляр базы данных.
        yclients (YClients): Экземпляр клиента API YClients.
    '''
    fullname = message.text.strip()  # type: ignore

    if not validate_fullname(fullname):
        await message.answer(
            messages.INVALID_FULLNAME,
            reply_markup=cancel_registration_keyboard(),
        )
        return

    parts = fullname.split()
    if len(parts) < 2:
        await message.answer(
            messages.INVALID_FULLNAME,
            reply_markup=cancel_registration_keyboard(),
        )
        return

    surname, name = parts[0], ' '.join(parts[1:])
    data = await state.get_data()
    phone = data.get('phone')

    await complete_registration(
        message,
        state,
        name,
        surname,
        phone,  # type: ignore
        db,
        yclients,
    )


@router.message(RegistrationStates.waiting_for_fullname)
async def invalid_fullname_data(message: types.Message):
    '''Отправляет сообщение об ошибке при некорректном вводе имени.

    Args:
        message (types.Message): Сообщение от пользователя.
    '''
    await message.answer(
        messages.INVALID_FULLNAME,
        reply_markup=cancel_registration_keyboard(),
    )


async def complete_registration(
    message: types.Message,
    state: FSMContext,
    name: str,
    surname: str,
    phone: str,
    db: Database,
    yclients: YClients,
):
    '''Завершает процесс регистрации и сохраняет данные пользователя.

    Args:
        message (types.Message): Сообщение от пользователя.
        state (FSMContext): Контекст состояния FSM.
        name (str): Имя пользователя.
        surname (str): Фамилия пользователя.
        phone (str): Телефонный номер пользователя.
        db (Database): Экземпляр базы данных.
        yclients (YClients): Экземпляр клиента API YClients.
    '''

    request_model = CreateClientRequest(
        body=CreateClientsRequestBody(
            name=name,
            surname=surname,
            patronymic='',
            phone=phone,
        ),
    )

    try:
        yclients_response = await yclients.clients.add_client(request_model=request_model)

        if yclients_response and yclients_response.success:
            yclients_id = yclients_response.data.id
        else:
            await message.answer(messages.REGISTRATION_YCLIENTS_ERROR)
            await state.clear()
            return
    except Exception:
        await message.answer(messages.REGISTRATION_ERROR)
        await state.clear()
        return

    await db.add_user(
        telegram_id=message.from_user.id,  # type: ignore
        name=name,
        patronymic='',
        surname=surname,
        phone=phone,
        yclients_id=yclients_id,
        thread_id=0,  # TODO: Тут будет ID потока OpenAI Assistants API
    )

    await message.answer(
        messages.REGISTRATION_SUCCESS.format(
            first_name=name,
            phone_number=phone,
        ),
        reply_markup=ReplyKeyboardRemove(),
    )
    await state.clear()


@router.callback_query(F.data == 'cancel_registration')
async def cancel_registration_callback(
    callback_query: types.CallbackQuery,
    state: FSMContext,
):
    '''Обрабатывает отмену регистрации через callback.

    Args:
        callback_query (types.CallbackQuery): Callback-запрос от пользователя.
        state (FSMContext): Контекст состояния FSM.
    '''
    await state.clear()
    await callback_query.message.edit_text(  # type: ignore
        messages.REGISTRATION_CANCELLED,
        reply_markup=main_menu_keyboard(),
    )
    await callback_query.answer()


@router.message(
    F.text == 'Отменить регистрацию',
    StateFilter(
        RegistrationStates.waiting_for_contact,
        RegistrationStates.waiting_for_fullname,
    ),
)
async def cancel_registration_message(
    message: types.Message,
    state: FSMContext,
):
    '''Обрабатывает отмену регистрации через сообщение.

    Args:
        message (types.Message): Сообщение от пользователя.
        state (FSMContext): Контекст состояния FSM.
    '''
    await state.clear()
    await message.answer(
        messages.REGISTRATION_CANCELLED,
        reply_markup=ReplyKeyboardRemove(),
    )


def register_registration_handlers(dp: Dispatcher):
    '''Регистрирует обработчики процесса регистрации.

    Args:
        dp (Dispatcher): Диспетчер для регистрации обработчиков.
    '''
    dp.include_router(router)
