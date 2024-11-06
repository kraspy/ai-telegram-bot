from ..common.base_service import BaseService
from ..common.enums import HTTPMethod

from .models import (
    GetClientsRequest,
    GetClientsResponse,
    CreateClientRequest,
    CreateClientResponse,
    BulkCreateClientsRequest,
    BulkCreateClientsResponse,
    GetClientCommentsRequest,
    GetClientRequest,
    VisitsSearchRequest,
    VisitsSearchResponse,
    GetClientResponse,
    UpdateClientRequest,
    UpdateClientResponse,
    DeleteClientRequest,
    DeleteClientResponse,
    GetClientCommentsResponse,
    CreateClientCommentRequest,
    CreateClientCommentResponse,
    DeleteClientCommentRequest,
    DeleteClientCommentResponse,
)


class ClientsService(BaseService):
    '''
    Сервис для работы с клиентами через API YClients.
    '''

    async def get_clients_list(
        self,
        request_model: GetClientsRequest,
    ) -> GetClientsResponse:
        '''
        Получить список клиентов.

        Args:
            request_model (GetClientsRequest): Модель данных запроса для поиска клиентов.

        Returns:
            GetClientsResponse: Модель ответа со списком клиентов.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/company/{self.manager.company_id}/clients/search'

        return await self.request_and_parse(
            method=HTTPMethod.POST,
            endpoint=endpoint,
            request_model=request_model,
            response_model=GetClientsResponse,
            use_user_token=True,
        )

    async def add_client(
        self,
        request_model: CreateClientRequest,
    ) -> CreateClientResponse:
        '''
        Добавить нового клиента.

        Args:
            request_model (CreateClientRequest): Модель данных нового клиента.

        Returns:
            CreateClientResponse: Модель ответа с информацией о созданном клиенте.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/clients/{self.manager.company_id}'

        return await self.request_and_parse(
            method=HTTPMethod.POST,
            endpoint=endpoint,
            request_model=request_model,
            response_model=CreateClientResponse,
            use_user_token=True,
        )

    async def bulk_add_clients(
        self,
        request_model: BulkCreateClientsRequest,
    ) -> BulkCreateClientsResponse:
        '''
        Массовое добавление клиентов.

        Args:
            request_model (BulkCreateClientsRequest): Модель данных для массового добавления клиентов.

        Returns:
            BulkCreateClientsResponse: Модель ответа с информацией о созданных клиентах и возможных ошибках.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/clients/{self.manager.company_id}/bulk'

        return await self.request_and_parse(
            method=HTTPMethod.POST,
            endpoint=endpoint,
            request_model=request_model,
            response_model=BulkCreateClientsResponse,
            use_user_token=True,
        )

    async def search_client_visits(
        self,
        request_model: VisitsSearchRequest,
    ) -> VisitsSearchResponse:
        '''
        Поиск по истории посещений клиентов.

        Args:
            request_model (VisitsSearchRequest): Модель данных для поиска визитов клиентов.

        Returns:
            VisitsSearchResponse: Модель ответа с информацией о визитах клиентов.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/company/{self.manager.company_id}/clients/visits/search'

        return await self.request_and_parse(
            method=HTTPMethod.POST,
            endpoint=endpoint,
            request_model=request_model,
            response_model=VisitsSearchResponse,
            use_user_token=True,
        )

    async def get_client(
        self,
        client_id: int,
        request_model: GetClientRequest | None = None,
    ) -> GetClientResponse:
        '''
        Получить данные клиента по его ID.

        Args:
            client_id (int): Идентификатор клиента.
            request_model (GetClientRequest | None): Модель данных запроса.

        Returns:
            GetClientResponse: Модель ответа с информацией о клиенте.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/client/{self.manager.company_id}/{client_id}'

        return await self.request_and_parse(
            method=HTTPMethod.POST,
            endpoint=endpoint,
            request_model=request_model,
            response_model=GetClientResponse,
            use_user_token=True,
        )

    async def update_client(
        self,
        client_id: int,
        request_model: UpdateClientRequest,
    ) -> UpdateClientResponse:
        '''
        Обновить данные клиента.

        Args:
            client_id (int): Идентификатор клиента.
            request_model (UpdateClientRequest): Модель данных для обновления клиента.

        Returns:
            UpdateClientResponse: Модель ответа с обновленными данными клиента.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/client/{self.manager.company_id}/{client_id}'

        return await self.request_and_parse(
            method=HTTPMethod.POST,
            endpoint=endpoint,
            request_model=request_model,
            response_model=UpdateClientResponse,
            use_user_token=True,
        )

    async def delete_client(
        self,
        client_id: int,
        request_model: DeleteClientRequest | None = None,
    ) -> DeleteClientResponse:
        '''
        Удалить клиента.

        Args:
            client_id (int): Идентификатор клиента.
            request_model (DeleteClientRequest | None): Модель данных для запроса.

        Returns:
            DeleteClientResponse: Модель ответа с результатом удаления клиента.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/client/{self.manager.company_id}/{client_id}'

        return await self.request_and_parse(
            method=HTTPMethod.DELETE,
            endpoint=endpoint,
            request_model=request_model,
            response_model=DeleteClientResponse,
            use_user_token=True,
        )

    async def get_client_comments(
        self,
        client_id: int,
        request_model: GetClientCommentsRequest | None = None,
    ) -> GetClientCommentsResponse:
        '''
        Получить список комментариев клиента.

        Args:
            client_id (int): Идентификатор клиента.
            request_model (GetClientCommentsRequest | None): Модель данных запроса.

        Returns:
            GetClientCommentsResponse: Модель ответа со списком комментариев клиента.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/company/{self.manager.company_id}/clients/{client_id}/comments'

        return await self.request_and_parse(
            method=HTTPMethod.POST,
            endpoint=endpoint,
            request_model=request_model,
            response_model=GetClientCommentsResponse,
            use_user_token=True,
        )

    async def create_client_comment(
        self,
        client_id: int,
        request_model: CreateClientCommentRequest,
    ) -> CreateClientCommentResponse:
        '''
        Добавить комментарий к клиенту.

        Args:
            client_id (int): Идентификатор клиента.
            request_model (CreateClientCommentRequest): Модель данных нового комментария.

        Returns:
            CreateClientCommentResponse: Модель ответа с информацией о созданном комментарии.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/company/{self.manager.company_id}/clients/{client_id}/comments'

        return await self.request_and_parse(
            method=HTTPMethod.POST,
            endpoint=endpoint,
            request_model=request_model,
            response_model=CreateClientCommentResponse,
            use_user_token=True,
        )

    async def delete_comment(
        self,
        client_id: int,
        comment_id: int,
        request_model: DeleteClientCommentRequest | None = None,
    ) -> DeleteClientCommentResponse:
        '''
        Удалить комментарий клиента.

        Args:
            client_id (int): Идентификатор клиента.
            comment_id (int): Идентификатор комментария.
            request_model (DeleteClientCommentRequest | None): Модель данных запроса.

        Returns:
            DeleteClientCommentResponse: Модель ответа с информацией об удалении комментария.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/company/{self.manager.company_id}/clients/{client_id}/comments/{comment_id}'

        return await self.request_and_parse(
            method=HTTPMethod.POST,
            endpoint=endpoint,
            request_model=request_model,
            response_model=DeleteClientCommentResponse,
            use_user_token=True,
        )
