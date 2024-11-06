from .models import (
    UserAuthRequest,
    UserAuthResponse,
    DeleteUserRecordRequest,
    DeleteUserRecordResponse,
    UserRecordsRequest,
    UserRecordsResponse,
)
from ..common.base_service import BaseService
from ..common.enums import HTTPMethod


class UserRecordService(BaseService):
    '''
    Сервис для работы с записями пользователя через API YClients.
    '''

    async def authorize_by_phone_and_code(
        self,
        request_model: UserAuthRequest,
    ) -> UserAuthResponse:
        '''
        Авторизация по номеру телефона и коду.

        Args:
            request_model (UserAuthRequest): Модель данных для авторизации.

        Returns:
            UserAuthResponse: Ответ с user_token пользователя.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = '/user/auth'

        return await self.request_and_parse(
            method=HTTPMethod.POST,
            endpoint=endpoint,
            request_model=request_model,
            response_model=UserAuthResponse,
            use_user_token=False,
        )

    async def get_user_records(
        self,
        record_id: int,
        record_hash: str,
        request_model: UserRecordsRequest,
    ) -> UserRecordsResponse:
        '''
        Получить записи пользователя.

        Args:
            record_id (int): ID записи.
            record_hash (str): HASH записи.
            request_model (UserRecordsRequest): Модель данных запроса.

        Returns:
            UserRecordsResponse: Ответ с данными о записях пользователя.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/user/records/{record_id}/{record_hash}'

        return await self.request_and_parse(
            method=HTTPMethod.GET,
            endpoint=endpoint,
            request_model=request_model,
            response_model=UserRecordsResponse,
            use_user_token=True,
        )

    async def delete_user_record(
        self,
        record_id: int,
        record_hash: str,
        request_model: DeleteUserRecordRequest,
    ) -> DeleteUserRecordResponse:
        '''
        Удалить запись пользователя.

        Args:
            record_id (int): ID записи.
            record_hash (str): HASH записи.
            request_model (DeleteUserRecordRequest): Модель данных запроса для удаления.

        Returns:
            DeleteUserRecordResponse: Ответ с результатом удаления.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/user/records/{record_id}/{record_hash}'

        return await self.request_and_parse(
            method=HTTPMethod.DELETE,
            endpoint=endpoint,
            request_model=request_model,
            response_model=DeleteUserRecordResponse,
            use_user_token=True,
        )
