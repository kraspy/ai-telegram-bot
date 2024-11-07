import aiosqlite
from datetime import datetime
import logging


class Database:
    '''
    Класс для работы с базой данных SQLite с использованием aiosqlite.
    '''

    def __init__(self, db_path: str):
        '''
        Инициализирует класс Database с указанным путём к файлу базы данных.

        Args:
            db_path (str): Путь к файлу базы данных SQLite.
        '''
        self.db_path = db_path
        self.logger = logging.getLogger(__name__)

    async def connect(self):
        '''
        Метод-заглушка для соответствия интерфейсу. В текущей реализации не требуется.
        '''
        self.logger.info('Connected to the SQLite database.')

    async def close(self):
        '''
        Метод-заглушка для соответствия интерфейсу. В текущей реализации не требуется.
        '''
        self.logger.info('Database connection closed.')

    async def create_tables(self):
        '''
        Создаёт таблицы `users` и `messages` в базе данных, если они не существуют.
        '''
        async with aiosqlite.connect(self.db_path) as conn:
            await conn.execute(
                '''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    telegram_id INTEGER UNIQUE NOT NULL,
                    yclients_id INTEGER,
                    thread_id INTEGER,
                    name TEXT NOT NULL,
                    patronymic TEXT,
                    surname TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    registered_at TIMESTAMP NOT NULL,
                    last_active TIMESTAMP NOT NULL
                );
                '''
            )
            await conn.execute(
                '''
                CREATE TABLE IF NOT EXISTS messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    message TEXT NOT NULL,
                    sender TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
                );
                '''
            )
            await conn.commit()
            self.logger.info('Database tables created or verified.')

    async def add_user(
        self,
        telegram_id: int,
        name: str,
        patronymic: str,
        surname: str,
        phone: str,
        yclients_id: int,
        thread_id: int,
    ):
        '''
        Добавляет нового пользователя в таблицу `users`.

        Args:
            telegram_id (int): Идентификатор пользователя в Telegram.
            name (str): Имя пользователя.
            patronymic (str): Отчество пользователя.
            surname (str): Фамилия пользователя.
            phone (str): Номер телефона пользователя.
            yclients_id (int): Идентификатор пользователя в системе YClients.
            thread_id (int): Идентификатор потока для асинхронной обработки.
        '''
        try:
            async with aiosqlite.connect(self.db_path) as conn:
                await conn.execute(
                    '''
                    INSERT OR IGNORE INTO users (
                      telegram_id, yclients_id, thread_id,
                      name, patronymic, surname, phone, registered_at, last_active
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
                    ''',
                    (
                        telegram_id,
                        yclients_id,
                        thread_id,
                        name,
                        patronymic,
                        surname,
                        phone,
                        datetime.utcnow(),
                        datetime.utcnow(),
                    ),
                )
                await conn.commit()
            self.logger.info(f'User {telegram_id} added to the database.')
        except Exception as e:
            self.logger.error(f'Error adding user {telegram_id}: {e}')

    async def get_user_by_telegram_id(self, telegram_id: int) -> dict | None:
        '''
        Получает пользователя из базы данных по его Telegram ID.

        Args:
            telegram_id (int): Идентификатор пользователя в Telegram.

        Returns:
            dict | None: Словарь с данными пользователя или None, если пользователь не найден.
        '''
        try:
            async with aiosqlite.connect(self.db_path) as conn:
                conn.row_factory = aiosqlite.Row
                async with conn.execute(
                    '''
                    SELECT * FROM users WHERE telegram_id = ?;
                    ''',
                    (telegram_id,),
                ) as cursor:
                    user = await cursor.fetchone()
                    if user:
                        user_dict = dict(user)
                        self.logger.info(f'User {telegram_id} retrieved from the database.')
                        return user_dict
                    self.logger.warning(f'User {telegram_id} not found in the database.')
                    return None
        except Exception as e:
            self.logger.error(f'Error retrieving user {telegram_id}: {e}')
            return None

    async def update_user_thread_id(self, telegram_id: int, thread_id: int) -> bool:
        '''
        Обновляет `thread_id` для пользователя.

        Args:
            telegram_id (int): Идентификатор пользователя в Telegram.
            thread_id (int): Новый идентификатор потока.

        Returns:
            bool: True, если обновление прошло успешно, иначе False.
        '''
        try:
            async with aiosqlite.connect(self.db_path) as conn:
                result = await conn.execute(
                    '''
                    UPDATE users SET thread_id = ?, last_active = ? WHERE telegram_id = ?;
                    ''',
                    (thread_id, datetime.utcnow(), telegram_id),
                )
                await conn.commit()
                if result.rowcount > 0:
                    self.logger.info(f'User {telegram_id} thread_id updated to {thread_id}.')
                    return True
                self.logger.warning(f'User {telegram_id} thread_id update failed.')
                return False
        except Exception as e:
            self.logger.error(f'Error updating thread_id for user {telegram_id}: {e}')
            return False

    async def update_user_data(self, telegram_id: int, name: str, patronymic: str, surname: str):
        '''
        Обновляет данные пользователя.

        Args:
            telegram_id (int): Идентификатор пользователя в Telegram.
            name (str): Новое имя пользователя.
            patronymic (str): Новое отчество пользователя.
            surname (str): Новая фамилия пользователя.
        '''
        try:
            async with aiosqlite.connect(self.db_path) as conn:
                await conn.execute(
                    '''
                    UPDATE users SET name = ?, patronymic = ?, surname = ?, last_active = ?
                    WHERE telegram_id = ?;
                    ''',
                    (name, patronymic, surname, datetime.utcnow(), telegram_id),
                )
                await conn.commit()
            self.logger.info(f'User {telegram_id} data updated.')
        except Exception as e:
            self.logger.error(f'Error updating data for user {telegram_id}: {e}')

    async def update_user_phone(self, telegram_id: int, phone: str):
        '''
        Обновляет номер телефона пользователя.

        Args:
            telegram_id (int): Идентификатор пользователя в Telegram.
            phone (str): Новый номер телефона пользователя.
        '''
        try:
            async with aiosqlite.connect(self.db_path) as conn:
                await conn.execute(
                    '''
                    UPDATE users SET phone = ?, last_active = ? WHERE telegram_id = ?;
                    ''',
                    (phone, datetime.utcnow(), telegram_id),
                )
                await conn.commit()
            self.logger.info(f'User {telegram_id} phone updated to {phone}.')
        except Exception as e:
            self.logger.error(f'Error updating phone for user {telegram_id}: {e}')

    async def add_message(self, user_id: int, message: str, sender: str):
        '''
        Добавляет сообщение в таблицу `messages`.

        Args:
            user_id (int): Идентификатор пользователя.
            message (str): Текст сообщения.
            sender (str): Отправитель сообщения.
        '''
        try:
            async with aiosqlite.connect(self.db_path) as conn:
                await conn.execute(
                    '''
                    INSERT INTO messages (user_id, message, sender, created_at)
                    VALUES (?, ?, ?, ?);
                    ''',
                    (user_id, message, sender, datetime.utcnow()),
                )
                await conn.commit()
            self.logger.info(f'Message added for user {user_id}.')
        except Exception as e:
            self.logger.error(f'Error adding message for user {user_id}: {e}')
