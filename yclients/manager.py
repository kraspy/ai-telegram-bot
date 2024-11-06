from typing import Any
import logging
import aiohttp
from aiohttp import ClientError
import orjson

from .services.common.enums import HTTPMethod
from .errors import (
    APIError,
    BadRequestError,
    UnauthorizedError,
    ForbiddenError,
    NotFoundError,
    UnprocessableEntityError,
)

logger = logging.getLogger(__name__)


def orjson_dumps(obj: Any) -> str:
    '''Сериализация объекта в JSON с помощью orjson.'''
    return orjson.dumps(obj).decode('utf-8')


class YClientsManager:
    '''
    Менеджер для работы с API YClients.

    Осуществляет выполнение HTTP-запросов к API YClients с использованием aiohttp.
    '''

    def __init__(
        self,
        api_url: str,
        partner_token: str,
        user_token: str | None,
        company_id: str,
        lang: str = 'ru-RU',
    ):
        '''
        Инициализирует менеджер YClientsManager.

        Args:
            api_url (str): URL API YClients.
            partner_token (str): Токен партнера для аутентификации.
            user_token (str | None): Токен пользователя для аутентификации. Может быть None.
            company_id (str): ID компании.
            lang (str, optional): Язык ответов API. По умолчанию - 'ru-RU'.
        '''
        self.api_url = api_url.rstrip('/')
        self.partner_token = partner_token
        self.user_token = user_token
        self.company_id = company_id
        self.lang = lang
        self.client = aiohttp.ClientSession(json_serialize=orjson_dumps)
        logger.info('YClientsManager инициализирован')

    def _get_headers(self, use_user_token: bool = True) -> dict[str, str]:
        '''
        Возвращает заголовки для запросов к API, включая токены авторизации.

        Args:
            use_user_token (bool, optional): Использовать ли токен пользователя. По умолчанию - True.

        Returns:
            dict[str, str]: Заголовки для запросов к API.
        '''
        headers = {
            'Accept': 'application/vnd.yclients.v2+json',
            'Accept-Language': self.lang,
            'Cache-Control': 'no-cache',
        }
        if use_user_token and self.user_token:
            headers['Authorization'] = f'Bearer {self.partner_token}, User {self.user_token}'
        else:
            headers['Authorization'] = f'Bearer {self.partner_token}'

        return headers

    def _handle_http_error(self, status_code: int, response_data: dict[str, Any]):
        '''
        Обрабатывает HTTP ошибки и выбрасывает соответствующие исключения.

        Args:
            status_code (int): HTTP статус код.
            response_data (dict[str, Any]): Данные ответа.

        Raises:
            BadRequestError: Ошибка 400.
            UnauthorizedError: Ошибка 401.
            ForbiddenError: Ошибка 403.
            NotFoundError: Ошибка 404.
            UnprocessableEntityError: Ошибка 422.
            APIError: Другие ошибки API.
        '''
        message = response_data.get('meta', {}).get('message', 'Unknown error')
        if status_code == 400:
            raise BadRequestError(message, status_code, response_data)
        elif status_code == 401:
            raise UnauthorizedError(message, status_code, response_data)
        elif status_code == 403:
            raise ForbiddenError(message, status_code, response_data)
        elif status_code == 404:
            raise NotFoundError(message, status_code, response_data)
        elif status_code == 422:
            raise UnprocessableEntityError(message, status_code, response_data)
        else:
            raise APIError(f'API returned unexpected status code {status_code}: {message}', status_code, response_data)

    async def _parse_response(self, response: aiohttp.ClientResponse) -> dict[str, Any]:
        '''
        Парсит ответ от сервера в словарь.

        Args:
            response (aiohttp.ClientResponse): Ответ от сервера.

        Returns:
            dict[str, Any]: Распарсенный ответ.
        '''
        content_type = response.headers.get('Content-Type', '')
        if 'application/json' in content_type:
            try:
                response_data = await response.json(loads=orjson.loads)
            except Exception as exc:
                logger.error(f'Error parsing JSON response: {exc}')
                response_data = {}
        else:
            response_text = await response.text()
            response_data = {'text': response_text}
        return response_data

    async def _make_request(
        self,
        method: HTTPMethod,
        endpoint: str,
        params: dict[str, Any] | None = None,
        data: dict[str, Any] | None = None,
        use_user_token: bool = True,
    ) -> dict[str, Any]:
        '''
        Выполняет HTTP-запрос к API YClients.

        Args:
            method (HTTPMethod): HTTP метод.
            endpoint (str): Конечная точка API.
            params (dict[str, Any] | None): Параметры запроса.
            data (dict[str, Any] | None): Данные для тела запроса.
            use_user_token (bool): Использовать ли токен пользователя.

        Returns:
            dict[str, Any]: Результат запроса в виде словаря.

        Raises:
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        url = f'{self.api_url}{endpoint}'
        headers = self._get_headers(use_user_token)
        try:
            logger.debug(f'Sending request: {method.value} {url}\nParams: {params}\nData: {data}')
            async with self.client.request(
                method.value,
                url,
                headers=headers,
                params=params,
                json=data,
            ) as response:
                response_data = await self._parse_response(response)

                if response.status in [200, 201, 202, 204]:
                    logger.debug(f'Successful response [{response.status}]: {response_data}')
                    return response_data
                else:
                    logger.error(f'Error response [{response.status}]: {response_data}')
                    self._handle_http_error(response.status, response_data)

        except ClientError as exc:
            logger.error(f'Aiohttp client error for URL {url}: {exc}')
            raise APIError(f'Client error during request to {url}: {exc}') from exc
        except Exception as e:
            logger.exception(f'Unexpected error during request to {url}')
            raise APIError(f'Unexpected error during request to {url}: {e}') from e

    async def close(self):
        '''Закрывает сессию aiohttp.ClientSession.'''
        if not self.client.closed:
            await self.client.close()
            logger.debug('Сессия aiohttp закрыта')
