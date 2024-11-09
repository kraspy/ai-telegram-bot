import asyncio
import logging
import logging.config
import yaml
from aiogram.exceptions import TelegramAPIError
from rich.traceback import install as rich_install
from bot.bot import create_bot_and_dispatcher


async def main():

    rich_install()

    with open('config/logging.yaml', 'r') as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)

    logger = logging.getLogger('bot_logger')

    bot, dp, yclients_manager, db = await create_bot_and_dispatcher()

    try:
        logger.info('Бот запущен...')

        await dp.start_polling(bot)
    except TelegramAPIError as e:
        logger.error(f'Telegram API Error: {e}')
    except Exception as e:
        logger.exception(f'Unexpected error: {e}')
    finally:
        logger.info('Бот завершает работу...')

        await bot.session.close()
        await yclients_manager.close()
        await db.close()

        logger.info('Бот успешно завершил работу.')


if __name__ == '__main__':
    asyncio.run(main())
