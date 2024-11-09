from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup

from bot.messages.messages import FAQ_ANSWERS, PRICE_QUESTIONS
from bot.utils.format import format_date, format_service_title

MAIN_MENU_BTN = InlineKeyboardButton(text='🏠 Главное меню', callback_data='main_menu')
SERVICES_BTN = InlineKeyboardButton(text='💆 Услуги', callback_data='menu_services')
BACK_TO_SERVICES_BTN = InlineKeyboardButton(text='⬅️ Назад', callback_data='menu_services')
BACK_TO_FAQ_BTN = InlineKeyboardButton(text='⬅️ Назад', callback_data='menu_faq')
BACK_TO_PRICES_BTN = InlineKeyboardButton(text='⬅️ Назад', callback_data='menu_prices')
BACK_TO_PRICES_QUESTIONS_BTN = InlineKeyboardButton(text='⬅️ Назад', callback_data='price_questions')


########################################################################################################################
# Клавиатуры регистрации
def cancel_registration_keyboard() -> InlineKeyboardMarkup:
    k = InlineKeyboardBuilder()
    k.button(text='Отменить регистрацию', callback_data='cancel_registration')
    return k.as_markup()


def registration_again_keyboard() -> InlineKeyboardMarkup:
    k = InlineKeyboardBuilder()
    k.button(text='✅ Зарегистрироваться', callback_data='registration_again')

    return k.as_markup()


########################################################################################################################
# Клавиатура главного меню
def main_menu_keyboard() -> InlineKeyboardMarkup:
    k = InlineKeyboardBuilder()

    # Блок с услугами
    k_services = InlineKeyboardBuilder()
    k_services.button(text='💆 Услуги', callback_data='menu_services')
    k_services.button(text='💲 Цены', callback_data='menu_prices')
    k.row(*k_services.buttons)

    # Другие кнопки
    k_other = InlineKeyboardBuilder()
    k_other.button(text='❓ Вопросы-ответы', callback_data='menu_faq')
    k_other.button(text='📞 Контакты', callback_data='menu_contacts')
    k.row(*k_other.buttons)

    return k.as_markup()


def back_to_home_keyboard() -> InlineKeyboardMarkup:
    k = InlineKeyboardBuilder()
    k.add(MAIN_MENU_BTN)

    return k.as_markup()


########################################################################################################################
# Клавиатуры для услуг и онлайн-записи
def make_an_appointment_keyboard(service_id: int) -> InlineKeyboardMarkup:
    k = InlineKeyboardBuilder()
    k.button(text='📅 Записаться', callback_data=f'book_service_{service_id}')
    k.add(BACK_TO_SERVICES_BTN)
    k.adjust(2)
    k.row(MAIN_MENU_BTN)

    return k.as_markup()


def services_keyboard(services) -> InlineKeyboardMarkup:
    k = InlineKeyboardBuilder()
    for service in services:
        formatted_title = format_service_title(service.title)
        k.button(text=f'{formatted_title}', callback_data=f'service_{service.id}')
    k.adjust(1)
    k.row(MAIN_MENU_BTN)

    return k.as_markup()


def back_to_services_keyboard() -> InlineKeyboardMarkup:
    k = InlineKeyboardBuilder()
    k.add(MAIN_MENU_BTN)
    k.add(SERVICES_BTN)
    k.adjust(2)

    return k.as_markup()


def back_to_service_keyboard() -> InlineKeyboardMarkup:
    k = InlineKeyboardBuilder()

    k.add(MAIN_MENU_BTN)
    k.adjust(2)

    return k.as_markup()


def dates_keyboard(dates) -> InlineKeyboardMarkup:
    k = InlineKeyboardBuilder()

    for date in dates:
        formatted_date = format_date(date)
        k.button(text=f'📅 {formatted_date}', callback_data=f'date_{date}')
    k.adjust(2)
    k.row(SERVICES_BTN, MAIN_MENU_BTN)

    return k.as_markup()


def times_keyboard(times) -> InlineKeyboardMarkup:
    k = InlineKeyboardBuilder()
    for time_slot in times:
        time_text = time_slot.time
        k.button(text=f'⏰ {time_text}', callback_data=f'time_{time_text}')
    k.adjust(4)
    k.row(SERVICES_BTN, MAIN_MENU_BTN)

    return k.as_markup()


def confirmation_keyboard() -> InlineKeyboardMarkup:
    k = InlineKeyboardBuilder()
    k.button(text='✅ Подтвердить', callback_data='confirm_yes')
    k.button(text='❌ Отменить', callback_data='confirm_no')
    k.adjust(2)
    return k.as_markup()


########################################################################################################################
# Клавиатуры для цен
def prices_menu_keyboard():
    k = InlineKeyboardBuilder()
    k.button(text='💰 Прайс-лист', callback_data='price_list')
    k.button(text='❓ Вопросы-ответы', callback_data='price_questions')
    k.adjust(2)
    k.row(MAIN_MENU_BTN)

    return k.as_markup()


def back_to_prices_keyboard() -> InlineKeyboardMarkup:
    k = InlineKeyboardBuilder()

    k.add(MAIN_MENU_BTN)
    k.add(BACK_TO_PRICES_BTN)
    k.adjust(2)

    return k.as_markup()


def prices_questions_keyboard() -> InlineKeyboardMarkup:
    k = InlineKeyboardBuilder()
    for question in PRICE_QUESTIONS:
        k.button(text=PRICE_QUESTIONS[question]['question'], callback_data=question)
    k.adjust(1)
    k.row(MAIN_MENU_BTN)

    return k.as_markup()


def back_to_prices_questions_keyboard() -> InlineKeyboardMarkup:
    k = InlineKeyboardBuilder()

    k.add(MAIN_MENU_BTN)
    k.add(BACK_TO_PRICES_QUESTIONS_BTN)
    k.adjust(2)

    return k.as_markup()


########################################################################################################################
# Клавиатуры FAQ
def faq_keyboard() -> InlineKeyboardMarkup:
    k = InlineKeyboardBuilder()
    for question in FAQ_ANSWERS:
        k.button(text=FAQ_ANSWERS[question]['question'], callback_data=question)
    k.adjust(1)
    k.row(MAIN_MENU_BTN)

    return k.as_markup()


def back_to_faq_keyboard() -> InlineKeyboardMarkup:
    k = InlineKeyboardBuilder()

    k.add(MAIN_MENU_BTN)
    k.add(SERVICES_BTN)
    k.adjust(2)

    return k.as_markup()


########################################################################################################################
# Клавиатуры контактов
def contacts_keyboard() -> InlineKeyboardMarkup:
    k = InlineKeyboardBuilder()
    k.button(text='📱 WhatsApp', url='https://wa.me/79330266161')
    k.button(text='💬 Telegram', url='https://t.me/krsk_cosmetolog')
    k.button(text='🌐 Instagram', url='https://www.instagram.com/cosmetolog_krsk_viktoria/')
    k.button(text='📘 VK', url='https://vk.com/id447028582')
    k.adjust(2)
    k.row(MAIN_MENU_BTN)

    return k.as_markup()
