from ..common.base_service import BaseService
from .models import (
    GetCommentsRequest,
    GetCommentsResponse,
    CreateCommentRequest,
    CreateCommentResponse,
)
from ..common.enums import HTTPMethod


class CommentsService(BaseService):
    '''
    Сервис для работы с комментариями через API YClients.
    '''

    async def get_comments(
        self,
        request_model: GetCommentsRequest,
    ) -> GetCommentsResponse:
        '''
        Получить список комментариев.

        Args:
            request_model (GetCommentsRequest): Параметры для фильтрации комментариев.

        Returns:
            GetCommentsResponse: Модель ответа с данными комментариев.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/comments/{self.manager.company_id}'

        return await self.request_and_parse(
            method=HTTPMethod.POST,
            endpoint=endpoint,
            request_model=request_model,
            response_model=GetCommentsResponse,
            use_user_token=True,
        )

    async def create_comment(
        self,
        staff_id: int,
        request_model: CreateCommentRequest,
    ) -> CreateCommentResponse:
        '''
        Оставить комментарий.

        Args:
            staff_id (int): Идентификатор сотрудника.
            request_model (CreateCommentRequest): Модель данных для создания комментария.

        Returns:
            CreateCommentResponse: Модель ответа с результатами создания комментария.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/comments/{self.manager.company_id}/{staff_id}'

        return await self.request_and_parse(
            method=HTTPMethod.POST,
            endpoint=endpoint,
            request_model=request_model,
            response_model=CreateCommentResponse,
            use_user_token=True,
        )
