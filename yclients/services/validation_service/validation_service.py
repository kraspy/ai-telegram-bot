from .models import (
    ValidatePhoneRequest,
    ValidatePhoneResponse,
)
from ..common.base_service import BaseService
from ..common.enums import HTTPMethod


class ValidationService(BaseService):
    '''
    Сервис для проверки формата номера телефона через API YClients.
    '''

    async def validate_phone(
        self,
        request_model: ValidatePhoneRequest,
        phone: str,
    ) -> ValidatePhoneResponse:
        '''
        Проверка формата номера телефона.

        Args:
            request_model (ValidatePhoneRequest): Модель данных для запроса.
            phone (str): Номер телефона для проверки в формате `+71234567890` или `71234567890`.

        Returns:
            ValidatePhoneResponse: Ответ API с результатом валидации номера телефона.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/validation/validate_phone/{phone}'

        return await self.request_and_parse(
            method=HTTPMethod.GET,
            endpoint=endpoint,
            request_model=request_model,
            response_model=ValidatePhoneResponse,
            use_user_token=True,
        )
