import asyncio
import logging
from datetime import datetime as dt
from datetime import date as d

import orjson
from aiogram import Bot
from aiogram.enums.chat_action import ChatAction
from openai import AsyncOpenAI

from yclients import YClients
from yclients.services.online_bookings_service.models import (
    BookableServicesQueryParams,
    BookableServicesRequest,
    BookableDatesQueryParams,
    BookableDatesRequest,
    BookableTimesQueryParams,
    BookableTimesRequest,
    BookRecordRequestBody,
    BookRecordRequest,
)
from yclients.services.online_bookings_service.models._additional import Appointment
from config.settings import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
assistant_id = settings.OPENAI_ASSISTANT_ID
model = settings.OPENAI_MODEL


class AssistantManager:
    '''Класс для управления ассистентом и взаимодействия с YClients API для конкретного пользователя.

    Атрибуты:
        client (AsyncOpenAI): Клиент OpenAI для взаимодействия с ассистентом.
        model (str): Модель OpenAI, используемая для ассистента.
        db: Объект базы данных для доступа к данным пользователя.
        yclients: Клиент YClients для взаимодействия с API YClients.
        user_id (int): Идентификатор пользователя.
        user_fullname (str): Полное имя пользователя.
        user_phone (str): Телефонный номер пользователя.
        assistant_id (str): Идентификатор ассистента OpenAI.
        thread_id (str): Идентификатор текущей сессии (thread) ассистента.
        assistant: Объект ассистента OpenAI.
        thread: Текущий поток сообщений ассистента.
        run: Текущий запуск (run) ассистента.
        lock (asyncio.Lock): Асинхронный lock для предотвращения одновременных запросов.
    '''

    def __init__(self, db, yclients, user_id):
        self.client = client
        self.model = model
        self.db = db
        self.yclients: YClients = yclients
        self.user_id = user_id
        self.user_fullname = None
        self.user_phone = None
        self.assistant_id = assistant_id
        self.thread_id = None
        self.assistant = None
        self.thread = None
        self.run = None
        self.lock = asyncio.Lock()

    @staticmethod
    async def get_datetime_now():
        '''Получает текущую дату и время в формате строки ISO 8601.

        Возвращает:
            str: Текущая дата и время в формате 'YYYY-MM-DDTHH:MM:SS'.
        '''
        return dt.now().strftime("%Y-%m-%dT%H:%M:%S")

    async def initialize(self):
        '''Инициализирует ассистента и поток сообщений для пользователя.

        Возвращает:
            str или None: Идентификатор потока сообщений или None в случае ошибки.
        '''
        try:
            if self.assistant_id:
                # Инициализация ассистента вынести за пределы try для сокращения вложенности
                self.assistant = await self.client.beta.assistants.retrieve(assistant_id=self.assistant_id)
                logger.info(f"Assistant {self.assistant_id} initialized successfully")

            user_data = await self.db.get_user_by_telegram_id(self.user_id)
            if user_data and user_data.get('thread_id'):
                self.thread_id = user_data['thread_id']
                self.user_fullname = f'{user_data["surname"]} {user_data["name"]}'
                self.user_phone = user_data['phone']
                # Объединить асинхронные вызовы для уменьшения количества обращений к API
                self.thread = await self.client.beta.threads.retrieve(thread_id=self.thread_id)
                logger.info(f"Thread {self.thread_id} retrieved for user {self.user_id}")
            else:
                self.thread = await self.client.beta.threads.create()
                self.thread_id = self.thread.id
                # Вынести обновление БД в отдельную функцию для лучшей читаемости
                await self.db.update_user_thread_id(self.user_id, self.thread_id)
                logger.info(f"New thread {self.thread_id} created for user {self.user_id}")

            return self.thread_id
        except Exception as e:
            logger.error(f"Error initializing assistant for user {self.user_id}: {str(e)}")
            return None

    async def cleanup(self):
        '''Очистка ресурсов (если необходимо).'''
        pass  # TODO: Реализовать, если будет необходимо

    async def add_message_to_thread_and_run(self, role, content, message, bot: Bot, user_data):
        '''Добавляет сообщение в поток и запускает ассистента.

        Параметры:
            role (str): Роль отправителя ('user' или 'assistant').
            content (str): Содержание сообщения.
            message: Сообщение Telegram.
            bot (Bot): Экземпляр бота.
            user_data: Данные пользователя.

        Возвращает:
            str: Ответ ассистента или сообщение об ошибке.
        '''
        if self.lock.locked():
            logger.info(f"Run already in progress for user {self.user_id}. Queuing message.")
            return 'Отвечаю на предыдущий вопрос ✨. Подождите, пожалуйста... 😊'
        async with self.lock:
            try:
                if not self.thread:
                    await self.initialize()

                await self.cancel_existing_runs()

                await self.client.beta.threads.messages.create(
                    thread_id=self.thread_id,  # type: ignore
                    role=role,
                    content=content,
                )

                current_datetime = await self.get_datetime_now()

                self.run = await self.client.beta.threads.runs.create(
                    thread_id=self.thread_id,  # type: ignore
                    assistant_id=self.assistant_id,  # type: ignore
                    additional_instructions=(
                        f'Клиент: {self.user_fullname}\n'
                        f'Номер телефона: {self.user_phone}\n'
                        f'Текущее время: {current_datetime}'
                    ),
                )
                logger.info(f"Run started for thread {self.thread_id}")

                return await self.handle_run(bot, message)
            except Exception as e:
                logger.error(f"Error adding message to thread for user {self.user_id}: {str(e)}")
                return 'Произошла ошибка при обработке вашего запроса.'

    async def cancel_existing_runs(self):
        '''Отменяет существующие запуски ассистента для текущего потока.'''
        try:
            runs = await self.client.beta.threads.runs.list(thread_id=self.thread_id)  # type: ignore
            for run in runs.data:
                if run.status not in ('expired', 'cancelled', 'completed'):
                    await self.client.beta.threads.runs.cancel(thread_id=self.thread_id, run_id=run.id)  # type: ignore
                    logger.info(f"Run {run.id} canceled for thread {self.thread_id}")
        except Exception as e:
            logger.error(f"Error canceling runs for thread {self.thread_id}: {str(e)}")

    async def handle_run(self, bot, message):
        '''Обрабатывает текущий запуск ассистента, ожидая его завершения.

        Параметры:
            bot (Bot): Экземпляр бота.
            message: Сообщение Telegram.

        Возвращает:
            str: Ответ ассистента или сообщение об ошибке.
        '''
        try:
            while True:
                # Уменьшить задержку ожидания и добавить прерывание цикла после нескольких итераций для избегания бесконечного цикла
                await bot.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)
                await asyncio.sleep(1.5)
                run_status = await self.client.beta.threads.runs.retrieve(
                    thread_id=self.thread_id,  # type: ignore
                    run_id=self.run.id,  # type: ignore
                )

                if run_status.status == 'completed':
                    messages = await self.client.beta.threads.messages.list(thread_id=self.thread_id)  # type: ignore
                    last_message = messages.data[0]
                    if last_message.role == 'assistant':
                        message_text = last_message.content[0].text.value  # type: ignore
                        logger.info(f"Assistant response: {message_text}")
                        return message_text
                elif run_status.status == 'requires_action':
                    await self.handle_required_actions(run_status.required_action.submit_tool_outputs)  # type: ignore
                elif run_status.status in ('canceled', 'expired', 'failed'):
                    return 'Произошла ошибка при обработке вашего запроса.'
        except Exception as e:
            logger.error(
                f"Error handling run for user {self.user_id}, status: {getattr(run_status, 'status', 'unknown')}: {str(e)}"
            )
            return 'Произошла ошибка при обработке вашего запроса.'

    async def handle_required_actions(self, required_action):
        '''Обрабатывает требуемые действия, вызванные ассистентом.

        Параметры:
            required_action: Объект требуемого действия (RequiredAction).
        '''
        try:
            tool_outputs = []
            for tool_call in required_action.tool_calls:
                function_name = tool_call.function.name
                arguments = orjson.loads(tool_call.function.arguments)
                function_response = await self.call_function(function_name, arguments)
                tool_outputs.append({'tool_call_id': tool_call.id, 'output': function_response})

            await self.client.beta.threads.runs.submit_tool_outputs(
                run_id=self.run.id,  # type: ignore
                thread_id=self.thread_id,  # type: ignore
                tool_outputs=tool_outputs,
            )
            logger.info(f"Tool outputs submitted for run {self.run.id}")  # type: ignore
        except Exception as e:
            logger.error(f"Error handling required actions for run {self.run.id}: {str(e)}")  # type: ignore

    async def call_function(self, function_name, arguments):
        '''Вызывает функцию по имени с заданными аргументами.

        Параметры:
            function_name (str): Имя функции для вызова.
            arguments (dict): Аргументы функции.

        Возвращает:
            dict или str: Результат выполнения функции или сообщение об ошибке.
        '''
        try:
            function_mapping = {
                'get_bookable_services': self.get_bookable_services,
                'get_bookable_dates': self.get_bookable_dates,
                'get_bookable_times': self.get_bookable_times,
                'create_book_record': self.create_book_record,
            }

            func = function_mapping.get(function_name)
            if func:
                # Логирование вызовов функций для отладки
                logger.debug(f"Calling function {function_name} with arguments {arguments}")
                return await func(arguments)
            else:
                logger.warning(f"Function {function_name} not implemented")
                return f"Функция {function_name} не реализована."
        except Exception as e:
            logger.error(f"Error calling function {function_name} with arguments {arguments}: {str(e)}")
            return f"Ошибка выполнения функции {function_name}"

    async def get_bookable_services(self, params):
        '''Получает список доступных для бронирования услуг из YClients API.

        Параметры:
            params (dict): Параметры запроса (не используются в данной реализации).

        Возвращает:
            str: JSON-строка с услугами или сообщение об ошибке.
        '''
        try:
            services_response = await self.yclients.online_bookings.get_bookable_services(
                BookableServicesRequest(
                    query=BookableServicesQueryParams(),
                ),
            )
            if services_response and services_response.success:
                services = services_response.data.services
                services_list = [
                    {'id': service.id, 'name': service.title, 'price_min': service.price_min} for service in services
                ]
                logger.info(f"Bookable services retrieved for user {self.user_id}")
                return orjson.dumps({'services': services_list}).decode('utf-8')
            else:
                return {'error': 'Не удалось получить список услуг.'}
        except Exception as e:
            logger.error(f"Error getting bookable services for user {self.user_id}: {str(e)}")
            return {'error': 'Не удалось получить список услуг.'}

    async def get_bookable_dates(self, params):
        '''Получает доступные даты для заданных услуг из YClients API.

        Параметры:
            params (dict): Параметры запроса, ожидается ключ 'service_ids' с списком ID услуг.

        Возвращает:
            str: JSON-строка с датами или сообщение об ошибке.
        '''
        try:
            service_ids = params.get('service_ids', [])
            if not service_ids:
                return {'error': 'Пожалуйста, укажите ID услуг.'}

            dates_response = await self.yclients.online_bookings.get_bookable_dates(
                BookableDatesRequest(
                    query=BookableDatesQueryParams(service_ids=service_ids),
                ),
            )
            if dates_response and dates_response.success:
                dates = dates_response.data.booking_dates
                dates_list = dates
                logger.info(f"Bookable dates retrieved for services {service_ids} for user {self.user_id}")
                return orjson.dumps({'dates': dates_list}).decode('utf-8')
            else:
                return {'error': 'Не удалось получить доступные даты.'}
        except Exception as e:
            logger.error(f"Error getting bookable dates for user {self.user_id}: {str(e)}")
            return {'error': 'Не удалось получить доступные даты.'}

    async def get_bookable_times(self, params):
        '''Получает доступное время для заданной даты и услуг из YClients API.

        Параметры:
            params (dict): Параметры запроса, ожидаются ключи 'staff_id', 'date', 'service_ids'.

        Возвращает:
            str: JSON-строка с временем или сообщение об ошибке.
        '''
        try:
            staff_id = params.get('staff_id')
            date = params.get('date')
            service_ids = params.get('service_ids', [])

            if not staff_id or not date or not service_ids:
                return {'error': 'Пожалуйста, укажите ID сотрудника, дату и ID услуг.'}

            times_response = await self.yclients.online_bookings.get_bookable_times(
                request_model=BookableTimesRequest(
                    query=BookableTimesQueryParams(),
                ),
                staff_id=staff_id,
                date=d.fromisoformat(date),
            )
            if times_response and times_response.success:
                times = times_response.data
                times_list = [{'time': time.time} for time in times]
                logger.info(
                    f"Bookable times retrieved for date {date} and services {service_ids} for user {self.user_id}"
                )
                return orjson.dumps({'times': times_list}).decode('utf-8')
            else:
                return {'error': 'Не удалось получить доступное время.'}
        except Exception as e:
            logger.error(f"Error getting bookable times for user {self.user_id}: {str(e)}")
            return {'error': 'Не удалось получить доступное время.'}

    async def create_book_record(self, params):
        '''Создает запись бронирования в YClients.

        Параметры:
            params (dict): Параметры запроса, ожидается ключ 'appointments' со списком записей.

        Возвращает:
            str: JSON-строка с подтверждением или сообщение об ошибке.
        '''
        try:
            appointment = params['appointments'][0]
            service_id = appointment.get('id')
            service_datetime = appointment.get('datetime')

            user_data = await self.db.get_user_by_telegram_id(self.user_id)
            if not user_data:
                return {'error': 'Пользователь не найден. Пожалуйста, зарегистрируйтесь.'}

            appointment_model = Appointment(
                id=1,
                services=[service_id],
                staff_id=3353649,  # Замените на актуальный ID сотрудника
                datetime=service_datetime,
            )
            booking_request = BookRecordRequest(
                body=BookRecordRequestBody(
                    phone=user_data['phone'],
                    email='',
                    fullname=f"{user_data['surname']} {user_data['name']} {user_data['patronymic']}",
                    appointments=[appointment_model],
                ),
            )
            booking_response = await self.yclients.online_bookings.create_book_record(booking_request)
            if booking_response and booking_response.success:
                logger.info(f"Booking created for user {self.user_id} at {service_datetime}")
                return orjson.dumps(
                    {'success': True, 'message': f"Запись успешно создана на {service_datetime}."},
                ).decode('utf-8')
            else:
                return {'error': 'Не удалось создать запись.'}
        except Exception as e:
            logger.error(f"Error creating book record for user {self.user_id}: {str(e)}")
            return {'error': 'Не удалось создать запись.'}
