from aiogram import Dispatcher, Router, types, F

from bot.keyboards.inline_keyboards import (
    prices_menu_keyboard,
    prices_questions_keyboard,
    back_to_prices_keyboard,
    back_to_prices_questions_keyboard,
    main_menu_keyboard,
)
from bot import messages

router = Router()


@router.callback_query(F.data == 'menu_prices')
async def send_prices_menu(callback_query: types.CallbackQuery):
    '''Отправляет меню с ценами при выборе соответствующего пункта.

    Args:
        callback_query (types.CallbackQuery): Callback-запрос от пользователя.
    '''
    await callback_query.message.edit_text(  # type: ignore
        messages.PRICE_LIST_INTRO,
        reply_markup=prices_menu_keyboard(),
    )
    await callback_query.answer()


@router.callback_query(F.data == 'price_list')
async def send_price_list(callback_query: types.CallbackQuery):
    '''Отправляет полный прайс-лист пользователю.

    Args:
        callback_query (types.CallbackQuery): Callback-запрос от пользователя.
    '''
    await callback_query.message.edit_text(  # type: ignore
        messages.PRICE_LIST,
        reply_markup=back_to_prices_keyboard(),
    )
    await callback_query.answer()


@router.callback_query(F.data == 'price_questions')
async def send_price_faq(callback_query: types.CallbackQuery):
    '''Отправляет список вопросов по ценам.

    Args:
        callback_query (types.CallbackQuery): Callback-запрос от пользователя.
    '''
    await callback_query.message.edit_text(  # type: ignore
        messages.PRICE_LIST_QUESTIONS_INTRO,
        reply_markup=prices_questions_keyboard(),
    )
    await callback_query.answer()


@router.callback_query(F.data.in_(messages.PRICE_QUESTIONS.keys()))
async def faq_response(callback_query: types.CallbackQuery):
    '''Отвечает на выбранный вопрос по ценам.

    Args:
        callback_query (types.CallbackQuery): Callback-запрос от пользователя.
    '''
    faq_key = callback_query.data

    if faq_key is None:
        return

    if question_data := messages.PRICE_QUESTIONS.get(faq_key):
        question = question_data['question']
        answer = question_data['answer']
        await callback_query.message.edit_text(  # type: ignore
            messages.PRICE_LIST_ANSWER.format(q=question, a=answer),
            reply_markup=back_to_prices_questions_keyboard(),
        )
    else:
        await callback_query.message.edit_text(  # type: ignore
            messages.UNKNOWN_COMMAND,
            reply_markup=main_menu_keyboard(),
        )
    await callback_query.answer()


def register_prices_handlers(dp: Dispatcher):
    '''Регистрирует обработчики цен в диспетчере.

    Args:
        dp (Dispatcher): Диспетчер для регистрации обработчиков.
    '''
    dp.include_router(router)
