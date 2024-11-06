from datetime import date
import logging
from .models import (
    BookableServicesRequest,
    BookableServicesResponse,
    BookableDatesRequest,
    BookableDatesResponse,
    BookableTimesRequest,
    BookableTimesResponse,
    CheckAppointmentsRequest,
    CheckAppointmentsResponse,
    BookRecordRequest,
    BookRecordResponse,
    RescheduleRecordRequest,
    RescheduleRecordResponse,
)
from ..common.base_service import BaseService
from ..common.enums import HTTPMethod

logger = logging.getLogger(__name__)


class OnlineBookingsService(BaseService):
    '''
    Сервис для работы с онлайн-записями через API YClients.
    '''

    async def get_bookable_services(
        self,
        request_model: BookableServicesRequest,
    ) -> BookableServicesResponse:
        '''
        Получение списка услуг, доступных для записи.

        Args:
            request_model (BookableServicesRequest): Модель данных запроса.

        Returns:
            BookableServicesResponse: Модель ответа со списком услуг, доступных для записи.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/book_services/{self.manager.company_id}'

        return await self.request_and_parse(
            method=HTTPMethod.GET,
            endpoint=endpoint,
            request_model=request_model,
            response_model=BookableServicesResponse,
            use_user_token=True,
        )

    async def get_bookable_dates(
        self,
        request_model: BookableDatesRequest,
    ) -> BookableDatesResponse:
        '''
        Получение списка доступных дат для записи.

        Args:
            request_model (BookableDatesRequest): Модель данных запроса.

        Returns:
            BookableDatesResponse: Модель ответа со списком доступных дат.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/book_dates/{self.manager.company_id}'

        return await self.request_and_parse(
            method=HTTPMethod.GET,
            endpoint=endpoint,
            request_model=request_model,
            response_model=BookableDatesResponse,
            use_user_token=True,
        )

    async def get_bookable_times(
        self,
        staff_id: int,
        date: date,
        request_model: BookableTimesRequest,
    ) -> BookableTimesResponse:
        '''
        Получение списка доступных временных слотов для записи на определённую дату и специалиста.

        Args:
            staff_id (int): ID специалиста.
            date (date): Дата для получения временных слотов.
            request_model (BookableTimesRequest): Модель данных запроса.

        Returns:
            BookableTimesResponse: Модель ответа со списком доступных временных слотов.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/book_times/{self.manager.company_id}/{staff_id}/{date.isoformat()}'

        return await self.request_and_parse(
            method=HTTPMethod.GET,
            endpoint=endpoint,
            request_model=request_model,
            response_model=BookableTimesResponse,
            use_user_token=True,
        )

    async def check_appointments(
        self,
        request_model: CheckAppointmentsRequest,
    ) -> CheckAppointmentsResponse:
        '''
        Проверка параметров записи.

        Args:
            request_model (CheckAppointmentsRequest): Модель данных для проверки записи.

        Returns:
            CheckAppointmentsResponse: Модель ответа проверки записи.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/book_record/{self.manager.company_id}/check'

        return await self.request_and_parse(
            method=HTTPMethod.POST,
            endpoint=endpoint,
            request_model=request_model,
            response_model=CheckAppointmentsResponse,
            use_user_token=True,
        )

    async def create_book_record(
        self,
        request_model: BookRecordRequest,
    ) -> BookRecordResponse:
        '''
        Создание записи на услугу.

        Args:
            request_model (BookRecordRequest): Модель запроса для создания записи.

        Returns:
            BookRecordResponse: Модель ответа создания записи.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/book_record/{self.manager.company_id}'

        return await self.request_and_parse(
            method=HTTPMethod.POST,
            endpoint=endpoint,
            request_model=request_model,
            response_model=BookRecordResponse,
            use_user_token=True,
        )

    async def reschedule_book_record(
        self,
        record_id: int,
        request_model: RescheduleRecordRequest,
    ) -> RescheduleRecordResponse:
        '''
        Перенос существующей записи на услугу.

        Args:
            record_id (int): ID записи, которую нужно перенести.
            request_model (RescheduleRecordRequest): Модель запроса для переноса записи.

        Returns:
            RescheduleRecordResponse: Модель ответа с данными о перенесенной записи.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/book_record/{self.manager.company_id}/{record_id}'

        return await self.request_and_parse(
            method=HTTPMethod.PUT,
            endpoint=endpoint,
            request_model=request_model,
            response_model=RescheduleRecordResponse,
            use_user_token=True,
        )
