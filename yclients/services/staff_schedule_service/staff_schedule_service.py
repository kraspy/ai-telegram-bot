from .models import (
    GetStaffScheduleRequest,
    GetStaffScheduleResponse,
    UpdateStaffScheduleRequest,
    UpdateStaffScheduleResponse,
)
from ..common.base_service import BaseService
from ..common.enums import HTTPMethod


class StaffScheduleService(BaseService):
    '''
    Сервис для работы с графиками работы сотрудников через API YClients.
    '''

    async def get_staff_schedule(
        self,
        request_model: GetStaffScheduleRequest,
    ) -> GetStaffScheduleResponse:
        '''
        Получение графиков работы сотрудников.

        Args:
            request_model (GetStaffScheduleRequest): Параметры для запроса расписания.

        Returns:
            GetStaffScheduleResponse: Ответ API с данными расписания.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/company/{self.manager.company_id}/staff/schedule'

        return await self.request_and_parse(
            method=HTTPMethod.GET,
            endpoint=endpoint,
            request_model=request_model,
            response_model=GetStaffScheduleResponse,
            use_user_token=True,
        )

    async def set_staff_schedule(
        self,
        request_model: UpdateStaffScheduleRequest,
    ) -> UpdateStaffScheduleResponse:
        '''
        Установка графиков работы сотрудников.

        Args:
            request_model (UpdateStaffScheduleRequest): Данные для установки графиков работы сотрудников,
                включая графики для установки и (опционально) для удаления.

        Returns:
            UpdateStaffScheduleResponse: Ответ API с результатом изменения графиков работы.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/company/{self.manager.company_id}/staff/schedule'

        return await self.request_and_parse(
            method=HTTPMethod.PUT,
            endpoint=endpoint,
            request_model=request_model,
            response_model=UpdateStaffScheduleResponse,
            use_user_token=True,
        )
