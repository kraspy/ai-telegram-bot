from aiogram import Dispatcher, Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from bot.keyboards.inline_keyboards import main_menu_keyboard
from bot import messages
from bot.handlers.registration import start_registration
from database import Database

router = Router()


@router.message(Command('start'))
async def cmd_start(message: types.Message, state: FSMContext, db: Database):
    '''Обрабатывает команду /start. Если пользователь не зарегистрирован, то отправляет ему сообщение о регистрации.

    Args:
        message (types.Message): Сообщение от пользователя.
        state (FSMContext): Контекст состояния FSM.
        db (Database): Экземпляр базы данных.
    '''
    user_data = await db.get_user_by_telegram_id(message.from_user.id)  # type: ignore
    if user_data:
        await message.answer(
            messages.MAIN_MENU.format(first_name=user_data['name']),
            reply_markup=main_menu_keyboard(),
        )
    else:
        await start_registration(message, state)


@router.message(F.text == 'F')  # TODO: Только для разработки
async def format_text(message: types.Message):
    '''Пример форматированного текста при получении текстового сообщения "F".

    Args:
        message (types.Message): Сообщение от пользователя.
    '''

    await message.answer(messages.FORMAT_TEXT)


def register_common_handlers(dp: Dispatcher):
    '''Регистрирует общие обработчики команд и сообщений.

    Args:
        dp (Dispatcher): Диспетчер для регистрации обработчиков.
    '''
    dp.include_router(router)
