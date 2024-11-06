import logging
from pydantic import ValidationError
from typing import TypeVar, Generic, Type

from yclients.manager import YClientsManager
from yclients.errors import APIError
from .enums import HTTPMethod
from .models import (
    BaseRequestModel,
    BaseResponseModel,
)

T = TypeVar('T', bound=BaseResponseModel)


class BaseService(Generic[T]):
    '''
    Базовый сервис для взаимодействия с API YClients.

    Содержит общие методы для выполнения запросов и обработки ответов.
    '''

    def __init__(self, manager: YClientsManager):
        '''
        Инициализирует базовый сервис с заданным менеджером.

        Args:
            manager (YClientsManager): Экземпляр менеджера YClientsManager.
        '''
        self.manager = manager
        self.logger = logging.getLogger(self.__class__.__name__)

    async def request_and_parse(
        self,
        method: HTTPMethod,
        endpoint: str,
        request_model: BaseRequestModel | None,
        response_model: Type[T],
        exclude_unset: bool = True,
        use_user_token: bool = True,
    ) -> T:
        '''
        Выполняет запрос к API и парсит ответ в заданную модель.

        Args:
            method (HTTPMethod): HTTP метод.
            endpoint (str): Конечная точка API.
            request_model (BaseRequestModel | None): Модель запроса или None.
            response_model (Type[T]): Класс модели для успешного ответа.
            exclude_unset (bool): Исключать ли неустановленные поля из запроса.
            use_user_token (bool): Использовать ли токен пользователя.

        Returns:
            T: Экземпляр модели ответа.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
            Exception: Для всех остальных исключений.
        '''
        body = (
            request_model.body.model_dump(
                exclude_unset=exclude_unset,
                by_alias=True,
            )
            if request_model and request_model.body
            else None
        )
        query_params = (
            request_model.query.model_dump(
                exclude_unset=exclude_unset,
                by_alias=True,
            )
            if request_model and request_model.query
            else None
        )
        try:
            self.logger.debug(
                f'🏗️ Preparing request: {method.value} {endpoint}\n' f'\tBody: {body}\n\tQuery Params: {query_params}'
            )

            response_data = await self.manager._make_request(
                method,
                endpoint,
                params=query_params,
                data=body,
                use_user_token=use_user_token,
            )

            parsed_response = response_model(**response_data)
            self.logger.debug(f'✅ Successful API response: {parsed_response}')
            return parsed_response

        except ValidationError as ve:
            self.logger.error(f'Validation Error ({response_model.__name__}): {ve}')
            raise ve

        except APIError as e:
            self.logger.error(f'API Error: {e}')
            raise e

        except Exception as e:
            self.logger.error(f'Unexpected error: {e}')
            raise e
