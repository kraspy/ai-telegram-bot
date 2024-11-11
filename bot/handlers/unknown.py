from aiogram import Router, Dispatcher, types

from bot import messages
from bot.keyboards.inline_keyboards import main_menu_keyboard

router = Router()


@router.message()
async def unknown_message(message: types.Message):
    '''Обрабатывает неизвестные команды и сообщения, отправляя стандартный ответ.

    Args:
        message (types.Message): Сообщение от пользователя.
    '''
    await message.answer(messages.UNKNOWN_COMMAND, reply_markup=main_menu_keyboard())


def register_unknown_handlers(dp: Dispatcher):
    '''Регистрирует обработчики для неизвестных команд в диспетчере.

    Args:
        dp (Dispatcher): Диспетчер для регистрации обработчиков.
    '''
    dp.include_router(router)
