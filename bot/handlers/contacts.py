from aiogram import Router, Dispatcher, types, F
from bot.keyboards.inline_keyboards import contacts_keyboard
from bot import messages

router = Router()


@router.callback_query(
    F.data == 'menu_contacts',
)
async def send_contacts(callback_query: types.CallbackQuery):
    '''Отправляет контактную информацию пользователю при выборе соответствующего пункта меню.

    Args:
        callback_query (types.CallbackQuery): Callback-запрос от пользователя.
    '''
    await callback_query.message.edit_text(  # type: ignore
        messages.CONTACTS,
        reply_markup=contacts_keyboard(),
    )
    await callback_query.answer()


def register_contacts_handlers(dp: Dispatcher):
    '''Регистрирует обработчики контактов в диспетчере.

    Args:
        dp (Dispatcher): Диспетчер для регистрации обработчиков.
    '''
    dp.include_router(router)
