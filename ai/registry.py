import asyncio
from .manager import AssistantManager
from database.database import Database
from yclients import YClients


class AssistantManagerRegistry:
    '''Класс для управления реестром AssistantManager для разных пользователей.

    Атрибуты:
        _registry (dict): Словарь, хранящий экземпляры AssistantManager по user_id.
        _lock (asyncio.Lock): Асинхронный замок для обеспечения потокобезопасности.
    '''

    def __init__(self):
        self._registry: dict[int, AssistantManager] = {}
        self._lock = asyncio.Lock()

    async def get_manager(self, db: Database, yclients: YClients, user_id: int) -> AssistantManager:
        '''Получает или создает AssistantManager для заданного пользователя.

        Параметры:
            db (Database): Экземпляр базы данных.
            yclients (YClients): Экземпляр клиента YClients API.
            user_id (int): Идентификатор пользователя Telegram.

        Возвращает:
            AssistantManager: Экземпляр AssistantManager для данного пользователя.
        '''
        async with self._lock:
            if user_id not in self._registry:
                self._registry[user_id] = AssistantManager(db, yclients, user_id)
            return self._registry[user_id]

    async def remove_manager(self, user_id: int):
        '''Удаляет AssistantManager для указанного пользователя из реестра.

        Параметры:
            user_id (int): Идентификатор пользователя Telegram.
        '''
        async with self._lock:
            if user_id in self._registry:
                del self._registry[user_id]


registry = AssistantManagerRegistry()
