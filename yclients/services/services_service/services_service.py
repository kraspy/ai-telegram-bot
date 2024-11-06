import logging

from .models import ServicesRequest, ServicesResponse
from ..common.base_service import BaseService
from ..common.enums import HTTPMethod

logger = logging.getLogger(__name__)


class ServicesService(BaseService):
    '''
    Сервис для работы с услугами через API YClients.
    '''

    async def get_services(
        self,
        request_model: ServicesRequest,
        service_id: int | None = None,
    ) -> ServicesResponse:
        '''
        Получение списка услуг или конкретной услуги.

        Args:
            request_model (ServicesRequest): Модель данных для запроса услуг.
            service_id (int | None, optional): Идентификатор конкретной услуги. Если не указан, возвращаются все услуги.

        Returns:
            ServicesResponse: Модель ответа со списком услуг или данными конкретной услуги.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''

        service_id_part = f'/{service_id}' if service_id is not None else ''
        endpoint = f'/company/{self.manager.company_id}/services{service_id_part}'

        return await self.request_and_parse(
            method=HTTPMethod.GET,
            endpoint=endpoint,
            request_model=request_model,
            response_model=ServicesResponse,
            use_user_token=True,
        )
