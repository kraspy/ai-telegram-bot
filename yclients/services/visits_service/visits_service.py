from .models import (
    GetVisitRequest,
    GetVisitResponse,
    GetVisitDetailsRequest,
    GetVisitDetailsResponse,
    UpdateVisitRequest,
    UpdateVisitResponse,
)
from ..common.base_service import BaseService
from ..common.enums import HTTPMethod


class VisitsService(BaseService):
    '''
    Сервис для работы с визитами через API YClients.
    '''

    async def get_visit(
        self,
        visit_id: int,
        request_model: GetVisitRequest,
    ) -> GetVisitResponse:
        '''
        Получить визит.

        Args:
            visit_id (int): Идентификатор визита.
            request_model (GetVisitRequest): Модель данных запроса.

        Returns:
            GetVisitResponse: Ответ API с данными визита.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/visits/{visit_id}'

        return await self.request_and_parse(
            method=HTTPMethod.GET,
            endpoint=endpoint,
            request_model=request_model,
            response_model=GetVisitResponse,
            use_user_token=True,
        )

    async def get_visit_details(
        self,
        salon_id: int,
        record_id: int,
        visit_id: int,
        request_model: GetVisitDetailsRequest,
    ) -> GetVisitDetailsResponse:
        '''
        Получить детали визита.

        Args:
            salon_id (int): Идентификатор салона.
            record_id (int): Идентификатор записи.
            visit_id (int): Идентификатор визита.
            request_model (GetVisitDetailsRequest): Модель данных запроса.

        Returns:
            GetVisitDetailsResponse: Ответ API с данными визита.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/visit/details/{salon_id}/{record_id}/{visit_id}'

        return await self.request_and_parse(
            method=HTTPMethod.GET,
            endpoint=endpoint,
            request_model=request_model,
            response_model=GetVisitDetailsResponse,
            use_user_token=True,
        )

    async def update_visit(
        self,
        visit_id: int,
        record_id: int,
        request_model: UpdateVisitRequest,
    ) -> UpdateVisitResponse:
        '''
        Изменить визит.

        Args:
            visit_id (int): Идентификатор визита.
            record_id (int): Идентификатор записи.
            request_model (UpdateVisitRequest): Данные для обновления визита.

        Returns:
            UpdateVisitResponse: Ответ API после успешного обновления визита.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/visits/{visit_id}/{record_id}'

        return await self.request_and_parse(
            method=HTTPMethod.PUT,
            endpoint=endpoint,
            request_model=request_model,
            response_model=UpdateVisitResponse,
            use_user_token=True,
        )
