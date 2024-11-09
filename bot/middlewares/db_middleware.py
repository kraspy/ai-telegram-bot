from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from typing import Callable, Dict, Any, Awaitable
from database.database import Database


class DbMiddleware(BaseMiddleware):
    '''Middleware для добавления экземпляра базы данных в данные события.'''

    def __init__(self, db: Database):
        super().__init__()
        self.db = db

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        '''Добавляет db в данные и вызывает обработчик.'''

        data['db'] = self.db
        return await handler(event, data)
