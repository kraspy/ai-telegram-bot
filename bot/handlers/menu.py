from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from bot.keyboards.inline_keyboards import main_menu_keyboard
from bot import messages
from bot.handlers.registration import start_registration
from database import Database

router = Router()


@router.message(F.text == 'Меню')
async def show_main_menu(
    message: types.Message,
    db: Database,
):
    '''Отображает главное меню при получении сообщения "Меню".

    Args:
        message (types.Message): Сообщение от пользователя.
        db (Database): Экземпляр базы данных.
    '''
    user_data = await db.get_user_by_telegram_id(message.from_user.id)  # type: ignore
    if user_data:
        await message.answer(
            messages.MAIN_MENU.format(first_name=user_data['name']),
            reply_markup=main_menu_keyboard(),
        )
    else:
        await start_registration(message, None)  # type: ignore


@router.callback_query(F.data == 'main_menu')
async def show_main_menu_callback(
    callback_query: types.CallbackQuery,
    db: Database,
    state: FSMContext,
):
    '''Обрабатывает нажатие кнопки "Главное меню" и отображает его.

    Args:
        callback_query (types.CallbackQuery): Callback-запрос от пользователя.
        db (Database): Экземпляр базы данных.
        state (FSMContext): Контекст состояния FSM.
    '''
    await state.clear()
    user_data = await db.get_user_by_telegram_id(callback_query.from_user.id)
    if user_data:
        await callback_query.message.edit_text(  # type: ignore
            messages.MAIN_MENU.format(first_name=user_data['name']),
            reply_markup=main_menu_keyboard(),
        )
    else:
        await start_registration(callback_query.message, None)  # type: ignore
    await callback_query.answer()


def register_menu_handlers(dp):
    '''Регистрирует обработчики меню в диспетчере.

    Args:
        dp: Диспетчер для регистрации обработчиков.
    '''
    dp.include_router(router)
