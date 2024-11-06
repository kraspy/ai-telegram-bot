from yclients.services.common.base_service import BaseService
from .models import (
    CreateRecordRequest,
    CreateRecordResponse,
    GetRecordsRequest,
    GetRecordsResponse,
    GetPartnerRecordsRequest,
    GetPartnerRecordsResponse,
    GetRecordRequest,
    GetRecordResponse,
    UpdateRecordRequest,
    UpdateRecordResponse,
    DeleteRecordRequest,
    DeleteRecordResponse,
)
from ..common.enums import HTTPMethod


class RecordsService(BaseService):
    '''
    Сервис для работы с записями через API YClients.
    '''

    async def get_records(
        self,
        request_model: GetRecordsRequest,
    ) -> GetRecordsResponse:
        '''
        Получить список записей для компании.

        Args:
            request_model (GetRecordsRequest): Модель данных запроса.

        Returns:
            GetRecordsResponse: Ответ API со списком записей.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/records/{self.manager.company_id}'

        return await self.request_and_parse(
            method=HTTPMethod.POST,
            endpoint=endpoint,
            request_model=request_model,
            response_model=GetRecordsResponse,
            use_user_token=True,
        )

    async def create_record(
        self,
        request_model: CreateRecordRequest,
    ) -> CreateRecordResponse:
        '''
        Создать новую запись.

        Args:
            request_model (CreateRecordRequest): Данные для создания новой записи.

        Returns:
            CreateRecordResponse: Ответ API с информацией о созданной записи.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/records/{self.manager.company_id}'

        return await self.request_and_parse(
            method=HTTPMethod.POST,
            endpoint=endpoint,
            request_model=request_model,
            response_model=CreateRecordResponse,
            use_user_token=True,
        )

    async def get_partner_records(
        self,
        request_model: GetPartnerRecordsRequest,
    ) -> GetPartnerRecordsResponse:
        '''
        Получить список записей партнёра.

        Args:
            request_model (GetPartnerRecordsRequest): Модель данных запроса.

        Returns:
            GetPartnerRecordsResponse: Ответ API со списком записей.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = '/records/partner'

        return await self.request_and_parse(
            method=HTTPMethod.POST,
            endpoint=endpoint,
            request_model=request_model,
            response_model=GetPartnerRecordsResponse,
            use_user_token=True,
        )

    async def get_record(
        self,
        record_id: int,
        request_model: GetRecordRequest,
    ) -> GetRecordResponse:
        '''
        Получить запись по её идентификатору.

        Args:
            record_id (int): Идентификатор записи.
            request_model (GetRecordRequest): Модель данных запроса.

        Returns:
            GetRecordResponse: Ответ API с данными записи.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/record/{self.manager.company_id}/{record_id}'

        return await self.request_and_parse(
            method=HTTPMethod.POST,
            endpoint=endpoint,
            request_model=request_model,
            response_model=GetRecordResponse,
            use_user_token=True,
        )

    async def update_record(
        self,
        record_id: int,
        request_model: UpdateRecordRequest,
    ) -> UpdateRecordResponse:
        '''
        Изменить запись.

        Args:
            record_id (int): Идентификатор записи.
            request_model (UpdateRecordRequest): Данные для обновления записи.

        Returns:
            UpdateRecordResponse: Ответ API с данными обновлённой записи.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/record/{self.manager.company_id}/{record_id}'

        return await self.request_and_parse(
            method=HTTPMethod.POST,
            endpoint=endpoint,
            request_model=request_model,
            response_model=UpdateRecordResponse,
            use_user_token=True,
        )

    async def delete_record(
        self,
        record_id: int,
        request_model: DeleteRecordRequest,
    ) -> DeleteRecordResponse:
        '''
        Удалить запись.

        Args:
            record_id (int): Идентификатор записи.
            request_model (DeleteRecordRequest): Модель данных запроса для удаления.

        Returns:
            DeleteRecordResponse: Ответ API после успешного удаления записи.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/record/{self.manager.company_id}/{record_id}'

        return await self.request_and_parse(
            method=HTTPMethod.POST,
            endpoint=endpoint,
            request_model=request_model,
            response_model=DeleteRecordResponse,
            use_user_token=True,
        )
