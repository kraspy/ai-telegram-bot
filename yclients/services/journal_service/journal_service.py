from datetime import date
from ..common.base_service import BaseService
from .models import (
    JournalDatesRequest,
    JournalDatesResponse,
    JournalSeancesRequest,
    JournalSeancesResponse,
)
from ..common.enums import HTTPMethod


class JournalService(BaseService):
    '''
    Сервис для работы с журналом расписания через API YClients.
    '''

    async def get_journal_dates(
        self,
        request_model: JournalDatesRequest,
        date: date,
    ) -> JournalDatesResponse:
        '''
        Получить список рабочих дат для указанной даты.

        Args:
            request_model (JournalDatesRequest): Модель данных запроса.
            date (date): Дата для получения рабочих дат.

        Returns:
            JournalDatesResponse: Ответ с данными о рабочих датах.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/timetable/dates/{self.manager.company_id}/{date.isoformat()}'

        return await self.request_and_parse(
            method=HTTPMethod.POST,
            endpoint=endpoint,
            request_model=request_model,
            response_model=JournalDatesResponse,
            use_user_token=True,
        )

    async def get_journal_seances(
        self,
        request_model: JournalSeancesRequest,
        staff_id: int,
        date: date,
    ) -> JournalSeancesResponse:
        '''
        Получить список сеансов для журнала.

        Args:
            request_model (JournalSeancesRequest): Модель данных запроса.
            staff_id (int): Идентификатор сотрудника.
            date (date): Дата для получения сеансов.

        Returns:
            JournalSeancesResponse: Ответ с данными о сеансах.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/timetable/seances/{self.manager.company_id}/{staff_id}/{date.isoformat()}'

        return await self.request_and_parse(
            method=HTTPMethod.POST,
            endpoint=endpoint,
            request_model=request_model,
            response_model=JournalSeancesResponse,
            use_user_token=True,
        )
