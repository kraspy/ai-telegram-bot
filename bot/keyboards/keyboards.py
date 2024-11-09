from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def cancel_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text='❌ Отменить регистрацию')
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)


def share_contact_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text='📲 Отправить контакт', request_contact=True)
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)
