from aiogram.utils.keyboard import ReplyKeyboardBuilder


########################################################################################################################
# Клавиатуры для регистрации
def cancel_keyboard():
    '''Клавиатура для отмены регистрации.

    Returns:
        ReplyKeyboardMarkup: Клавиатура с кнопкой "Отменить регистрацию".
    '''
    builder = ReplyKeyboardBuilder()
    builder.button(text='❌ Отменить регистрацию')
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)


def share_contact_keyboard():
    '''Клавиатура для отправки контакта.

    Returns:
        ReplyKeyboardMarkup: Клавиатура с кнопкой "Отправить контакт".
    '''
    builder = ReplyKeyboardBuilder()
    builder.button(text='📲 Отправить контакт', request_contact=True)
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)
