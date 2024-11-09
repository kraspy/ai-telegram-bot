from aiogram import BaseMiddleware
from typing import Callable, Dict, Any, Awaitable


class YClientsMiddleware(BaseMiddleware):
    '''Middleware для добавления yclients_manager в данные события.'''

    def __init__(self, yclients_manager):
        super().__init__()
        self.yclients_manager = yclients_manager

    async def __call__(
        self,
        handler: Callable[[Any, Dict[str, Any]], Awaitable[Any]],
        event: Any,
        data: Dict[str, Any],
    ) -> Any:
        '''Добавляет yclients_manager в данные и вызывает обработчик.'''

        data['yclients'] = self.yclients_manager
        return await handler(event, data)
