from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.messages.messages import FAQ_ANSWERS, PRICE_QUESTIONS
from bot.utils.format import format_date, format_service_title

BACK_BTN_TEXT = '⬅️ Назад'

# Кнопки
MAIN_MENU_BTN = InlineKeyboardButton(
    text='🏠 Главное меню',
    callback_data='main_menu',
)
SERVICES_BTN = InlineKeyboardButton(
    text='💆 Услуги',
    callback_data='menu_services',
)
BACK_TO_SERVICES_BTN = InlineKeyboardButton(
    text=BACK_BTN_TEXT,
    callback_data='menu_services',
)
BACK_TO_FAQ_BTN = InlineKeyboardButton(
    text=BACK_BTN_TEXT,
    callback_data='menu_faq',
)
BACK_TO_PRICES_BTN = InlineKeyboardButton(
    text=BACK_BTN_TEXT,
    callback_data='menu_prices',
)
BACK_TO_PRICES_QUESTIONS_BTN = InlineKeyboardButton(
    text=BACK_BTN_TEXT,
    callback_data='price_questions',
)


########################################################################################################################
# Клавиатуры регистрации
def cancel_registration_keyboard():
    '''Клавиатура для отмены регистрации.

    Returns:
        InlineKeyboardMarkup: Клавиатура с кнопкой отмены регистрации.
    '''
    builder = InlineKeyboardBuilder()
    builder.button(text='❌ Отменить регистрацию', callback_data='cancel_registration')
    return builder.as_markup()


def registration_again_keyboard():
    '''Клавиатура для повторной регистрации.

    Returns:
        InlineKeyboardMarkup: Клавиатура с кнопкой повторной регистрации.
    '''
    builder = InlineKeyboardBuilder()
    builder.button(text='✅ Зарегистрироваться', callback_data='registration_again')
    return builder.as_markup()


########################################################################################################################
# Клавиатура главного меню
def main_menu_keyboard():
    '''Создает клавиатуру главного меню.

    Returns:
        InlineKeyboardMarkup: Клавиатура главного меню.
    '''
    builder = InlineKeyboardBuilder()
    builder.button(text='💆 Услуги', callback_data='menu_services')
    builder.button(text='💲 Цены', callback_data='menu_prices')
    builder.button(text='❓ Вопросы-ответы', callback_data='menu_faq')
    builder.button(text='📞 Контакты', callback_data='menu_contacts')
    builder.adjust(2)
    return builder.as_markup()


def back_to_home_keyboard():
    '''Клавиатура для возврата на главное меню.

    Returns:
        InlineKeyboardMarkup: Клавиатура с кнопкой "Главное меню".
    '''
    builder = InlineKeyboardBuilder()
    builder.add(MAIN_MENU_BTN)
    return builder.as_markup()


########################################################################################################################
# Клавиатуры для услуг и онлайн-записи
def make_an_appointment_keyboard(service_id):
    '''Клавиатура для записи на услугу.

    Args:
        service_id (int): Идентификатор услуги.

    Returns:
        InlineKeyboardMarkup: Клавиатура с кнопкой записи и кнопкой назад.
    '''
    builder = InlineKeyboardBuilder()
    builder.button(text='📅 Записаться', callback_data=f'book_service_{service_id}')
    builder.add(BACK_TO_SERVICES_BTN)
    builder.adjust(1)
    builder.row(MAIN_MENU_BTN)
    return builder.as_markup()


def services_keyboard(services):
    '''Клавиатура со списком услуг.

    Args:
        services (list): Список доступных услуг.

    Returns:
        InlineKeyboardMarkup: Клавиатура с услугами.
    '''
    builder = InlineKeyboardBuilder()
    for service in services:
        formatted_title = format_service_title(service.title)
        builder.button(text=formatted_title, callback_data=f'service_{service.id}')
    builder.adjust(1)
    builder.row(MAIN_MENU_BTN)
    return builder.as_markup()


def back_to_services_keyboard():
    '''Клавиатура для возврата к услугам.

    Returns:
        InlineKeyboardMarkup: Клавиатура с кнопками "Главное меню" и "Услуги".
    '''
    builder = InlineKeyboardBuilder()
    builder.add(MAIN_MENU_BTN)
    builder.add(SERVICES_BTN)
    builder.adjust(2)
    return builder.as_markup()


def dates_keyboard(dates):
    '''Клавиатура с доступными датами.

    Args:
        dates (list): Список доступных дат.

    Returns:
        InlineKeyboardMarkup: Клавиатура с датами.
    '''
    builder = InlineKeyboardBuilder()
    for date in dates:
        formatted_date = format_date(date)
        builder.button(text=f'📅 {formatted_date}', callback_data=f'date_{date}')
    builder.adjust(2)
    builder.row(SERVICES_BTN, MAIN_MENU_BTN)
    return builder.as_markup()


def times_keyboard(times):
    '''Клавиатура с доступным временем.

    Args:
        times (list): Список доступного времени.

    Returns:
        InlineKeyboardMarkup: Клавиатура с временем.
    '''
    builder = InlineKeyboardBuilder()
    for time_slot in times:
        time_text = time_slot.time
        builder.button(text=f'⏰ {time_text}', callback_data=f'time_{time_text}')
    builder.adjust(4)
    builder.row(SERVICES_BTN, MAIN_MENU_BTN)
    return builder.as_markup()


def confirmation_keyboard():
    '''Клавиатура подтверждения записи.

    Returns:
        InlineKeyboardMarkup: Клавиатура с кнопками "Подтвердить" и "Отменить".
    '''
    builder = InlineKeyboardBuilder()
    builder.button(text='✅ Подтвердить', callback_data='confirm_yes')
    builder.button(text='❌ Отменить', callback_data='confirm_no')
    builder.adjust(2)
    return builder.as_markup()


########################################################################################################################
# Клавиатуры для цен
def prices_menu_keyboard():
    '''Клавиатура меню цен.

    Returns:
        InlineKeyboardMarkup: Клавиатура с кнопками прайс-листа и вопросов.
    '''
    builder = InlineKeyboardBuilder()
    builder.button(text='💰 Прайс-лист', callback_data='price_list')
    builder.button(text='❓ Вопросы-ответы', callback_data='price_questions')
    builder.adjust(2)
    builder.row(MAIN_MENU_BTN)
    return builder.as_markup()


def back_to_prices_keyboard():
    '''Клавиатура для возврата к меню цен.

    Returns:
        InlineKeyboardMarkup: Клавиатура с кнопками "Главное меню" и "Назад".
    '''
    builder = InlineKeyboardBuilder()
    builder.add(MAIN_MENU_BTN)
    builder.add(BACK_TO_PRICES_BTN)
    builder.adjust(2)
    return builder.as_markup()


def prices_questions_keyboard():
    '''Клавиатура с вопросами о ценах.

    Returns:
        InlineKeyboardMarkup: Клавиатура с вопросами.
    '''
    builder = InlineKeyboardBuilder()
    for question_key, question_data in PRICE_QUESTIONS.items():
        builder.button(text=question_data['question'], callback_data=question_key)
    builder.adjust(1)
    builder.row(MAIN_MENU_BTN)
    return builder.as_markup()


def back_to_prices_questions_keyboard():
    '''Клавиатура для возврата к вопросам о ценах.

    Returns:
        InlineKeyboardMarkup: Клавиатура с кнопками "Главное меню" и "Назад".
    '''
    builder = InlineKeyboardBuilder()
    builder.add(MAIN_MENU_BTN)
    builder.add(BACK_TO_PRICES_QUESTIONS_BTN)
    builder.adjust(2)
    return builder.as_markup()


########################################################################################################################
# Клавиатуры FAQ
def faq_keyboard():
    '''Клавиатура с часто задаваемыми вопросами.

    Returns:
        InlineKeyboardMarkup: Клавиатура с вопросами FAQ.
    '''
    builder = InlineKeyboardBuilder()
    for question_key, question_data in FAQ_ANSWERS.items():
        builder.button(text=question_data['question'], callback_data=question_key)
    builder.adjust(1)
    builder.row(MAIN_MENU_BTN)
    return builder.as_markup()


def back_to_faq_keyboard():
    '''Клавиатура для возврата к FAQ.

    Returns:
        InlineKeyboardMarkup: Клавиатура с кнопками "Главное меню" и "Услуги".
    '''
    builder = InlineKeyboardBuilder()
    builder.add(MAIN_MENU_BTN)
    builder.add(SERVICES_BTN)
    builder.adjust(2)
    return builder.as_markup()


########################################################################################################################
# Клавиатуры контактов
def contacts_keyboard():
    '''Клавиатура с контактами.

    Returns:
        InlineKeyboardMarkup: Клавиатура с кнопками социальных сетей и мессенджеров.
    '''
    builder = InlineKeyboardBuilder()
    builder.button(text='📱 WhatsApp', url='https://wa.me/79330266161')
    builder.button(text='💬 Telegram', url='https://t.me/krsk_cosmetolog')
    builder.button(text='🌐 Instagram', url='https://www.instagram.com/cosmetolog_krsk_viktoria/')
    builder.button(text='📘 VK', url='https://vk.com/id447028582')
    builder.adjust(2)
    builder.row(MAIN_MENU_BTN)
    return builder.as_markup()
