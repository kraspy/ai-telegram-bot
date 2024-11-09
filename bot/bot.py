from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot.handlers import register_handlers
from bot.middlewares import YClientsMiddleware, DbMiddleware
from yclients import YClients, YClientsManager
from database import initialize_database

from config import settings


async def create_bot_and_dispatcher():
    '''Создает и настраивает экземпляры бота и диспетчера.

    Возвращает:
        tuple: Бот, диспетчер, экземпляр YClients и экземпляр базы данных.

    Вызывает:
        ValueError: Если отсутствуют необходимые настройки.
    '''
    if not hasattr(settings, 'TELEGRAM_BOT_TOKEN') or not settings.TELEGRAM_BOT_TOKEN:
        raise ValueError('TELEGRAM_BOT_TOKEN is not set in settings.')

    bot = Bot(token=settings.TELEGRAM_BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=MemoryStorage())

    if not hasattr(settings, 'YCLIENTS_API_URL') or not settings.YCLIENTS_API_URL:
        raise ValueError('YCLIENTS_API_URL is not set in settings.')

    if not hasattr(settings, 'YCLIENTS_PARTNER_TOKEN') or not settings.YCLIENTS_PARTNER_TOKEN:
        raise ValueError('YCLIENTS_PARTNER_TOKEN is not set in settings.')

    if not hasattr(settings, 'YCLIENTS_USER_TOKEN') or not settings.YCLIENTS_USER_TOKEN:
        raise ValueError('YCLIENTS_USER_TOKEN is not set in settings.')

    if not hasattr(settings, 'YCLIENTS_COMPANY_ID') or not settings.YCLIENTS_COMPANY_ID:
        raise ValueError('YCLIENTS_COMPANY_ID is not set in settings.')

    yclients_manager = YClientsManager(
        api_url=settings.YCLIENTS_API_URL,
        partner_token=settings.YCLIENTS_PARTNER_TOKEN,
        user_token=settings.YCLIENTS_USER_TOKEN,
        company_id=settings.YCLIENTS_COMPANY_ID,
    )

    yclients = YClients(yclients_manager)
    db = await initialize_database()

    dp.message.middleware(DbMiddleware(db))
    dp.callback_query.middleware(DbMiddleware(db))
    dp.message.middleware(YClientsMiddleware(yclients))
    dp.callback_query.middleware(YClientsMiddleware(yclients))

    register_handlers(dp)

    return bot, dp, yclients, db
