from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from bot.states.states import FAQStates
from bot.keyboards.inline_keyboards import (
    faq_keyboard,
    back_to_faq_keyboard,
    main_menu_keyboard,
)
from bot import messages

router = Router()


@router.callback_query(F.data == 'menu_faq')
async def send_faq(callback_query: types.CallbackQuery, state: FSMContext):
    '''Отправляет список часто задаваемых вопросов пользователю.

    Args:
        callback_query (types.CallbackQuery): Callback-запрос от пользователя.
        state (FSMContext): Контекст состояния FSM.
    '''
    await callback_query.message.edit_text(  # type: ignore
        messages.FAQ_INTRO,
        reply_markup=faq_keyboard(),
    )
    await state.set_state(FAQStates.choosing_faq)
    await callback_query.answer()


@router.callback_query(
    FAQStates.choosing_faq,
    F.data.startswith('faq_'),
)
async def faq_response(callback_query: types.CallbackQuery, state: FSMContext):
    '''Обрабатывает выбор пользователя в разделе FAQ и отправляет соответствующий ответ.

    Args:
        callback_query (types.CallbackQuery): Callback-запрос от пользователя.
        state (FSMContext): Контекст состояния FSM.
    '''
    faq_number = callback_query.data

    if not callback_query.message:
        return

    if faq_number is None:
        return

    if question := messages.FAQ_ANSWERS.get(faq_number):
        await callback_query.message.edit_text(  # type: ignore
            messages.FAQ_QUESTION.format(
                q=question['question'],
                a=question['answer'],
            ),
            reply_markup=back_to_faq_keyboard(),
        )
        await state.clear()
    else:
        await callback_query.message.edit_text(  # type: ignore
            messages.UNKNOWN_COMMAND,
            reply_markup=main_menu_keyboard(),
        )
    await callback_query.answer()


def register_faq_handlers(dp):
    '''Регистрирует обработчики раздела FAQ в диспетчере.

    Args:
        dp: Диспетчер для регистрации обработчиков.
    '''
    dp.include_router(router)
