import asyncio
import logging
from aiogram import Dispatcher, Router, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from bot.keyboards.inline_keyboards import main_menu_keyboard
from bot import messages
from bot.states.states import RegistrationStates
from bot.handlers.registration import start_registration
from bot.utils.md_utils import markdown_to_telegram_html
from yclients import YClients
from bot.bot import Bot
from database import Database
from ai.registry import registry as ai_registry


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


@router.message(~StateFilter(RegistrationStates.waiting_for_fullname), F.text)
async def user_text(message: types.Message, state: FSMContext, db: Database, bot: Bot, yclients: YClients):
    user_data = await db.get_user_by_telegram_id(message.from_user.id)  # type: ignore
    if user_data:
        await bot.send_chat_action(message.chat.id, 'typing')
        await asyncio.sleep(1)

        assistant = await ai_registry.get_manager(
            db=db,
            yclients=yclients,
            user_id=message.from_user.id,  # type: ignore
        )
        await assistant.initialize()

        content = message.text

        await db.add_message(user_data['id'], content, 'user')  # type: ignore

        answer = await assistant.add_message_to_thread_and_run(
            role='user', content=content, message=message, bot=bot, user_data=user_data
        )

        html_answer = markdown_to_telegram_html(answer)

        await db.add_message(0, html_answer, 'assistant')
        logging.info(html_answer)

        # await message.answer(html_answer, reply_markup=main_menu_keyboard())
        await message.answer(html_answer)

    else:
        await start_registration(message, state)


def register_common_handlers(dp: Dispatcher):
    '''Регистрирует общие обработчики команд и сообщений.

    Args:
        dp (Dispatcher): Диспетчер для регистрации обработчиков.
    '''
    dp.include_router(router)
