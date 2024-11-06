from .models import (
    SmsClientsByIdRequest,
    SmsClientsByIdResponse,
    SmsClientsByFilterRequest,
    SmsClientsByFilterResponse,
    EmailClientsByIdRequest,
    EmailClientsByIdResponse,
    EmailClientsByFilterRequest,
    EmailClientsByFilterResponse,
    SmsSendRequest,
    SmsSendResponse,
    DeliveryStatusRequest,
    DeliveryStatusResponse,
)
from ..common.base_service import BaseService
from ..common.enums import HTTPMethod


class NewsletterService(BaseService):
    '''
    Сервис для работы с рассылками через API YClients.
    '''

    async def send_sms_by_id(
        self,
        request_model: SmsClientsByIdRequest,
    ) -> SmsClientsByIdResponse:
        '''
        Отправить SMS рассылку по списку клиентов.

        Args:
            request_model (SmsClientsByIdRequest): Модель данных для SMS рассылки.

        Returns:
            SmsClientsByIdResponse: Модель ответа с результатами отправки SMS.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/sms/clients/by_id/{self.manager.company_id}'

        return await self.request_and_parse(
            method=HTTPMethod.POST,
            endpoint=endpoint,
            request_model=request_model,
            response_model=SmsClientsByIdResponse,
            use_user_token=True,
        )

    async def send_sms_by_filter(
        self,
        request_model: SmsClientsByFilterRequest,
    ) -> SmsClientsByFilterResponse:
        '''
        Отправить SMS рассылку по клиентам, подходящим под фильтры.

        Args:
            request_model (SmsClientsByFilterRequest): Модель данных для SMS рассылки.

        Returns:
            SmsClientsByFilterResponse: Модель ответа с результатами отправки SMS.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/sms/clients/by_filter/{self.manager.company_id}'

        return await self.request_and_parse(
            method=HTTPMethod.POST,
            endpoint=endpoint,
            request_model=request_model,
            response_model=SmsClientsByFilterResponse,
            use_user_token=True,
        )

    async def send_email_by_id(
        self,
        request_model: EmailClientsByIdRequest,
    ) -> EmailClientsByIdResponse:
        '''
        Отправить Email рассылку по списку клиентов.

        Args:
            request_model (EmailClientsByIdRequest): Модель данных для Email рассылки.

        Returns:
            EmailClientsByIdResponse: Модель ответа с результатами отправки Email.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/email/clients/by_id/{self.manager.company_id}'

        return await self.request_and_parse(
            method=HTTPMethod.POST,
            endpoint=endpoint,
            request_model=request_model,
            response_model=EmailClientsByIdResponse,
            use_user_token=True,
        )

    async def send_email_by_filter(
        self,
        request_model: EmailClientsByFilterRequest,
    ) -> EmailClientsByFilterResponse:
        '''
        Отправить Email рассылку по клиентам, подходящим под фильтры.

        Args:
            request_model (EmailClientsByFilterRequest): Модель данных и фильтров для рассылки Email.

        Returns:
            EmailClientsByFilterResponse: Модель ответа с результатами рассылки.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = f'/email/clients/by_filter/{self.manager.company_id}'

        return await self.request_and_parse(
            method=HTTPMethod.POST,
            endpoint=endpoint,
            request_model=request_model,
            response_model=EmailClientsByFilterResponse,
            use_user_token=True,
        )

    async def send_sms(
        self,
        request_model: SmsSendRequest,
    ) -> SmsSendResponse:
        '''
        Отправка SMS через операторов.

        Args:
            request_model (SmsSendRequest): Модель данных для отправки SMS.

        Returns:
            SmsSendResponse: Модель ответа с данными о результате отправки.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = '/sms/send'

        return await self.request_and_parse(
            method=HTTPMethod.POST,
            endpoint=endpoint,
            request_model=request_model,
            response_model=SmsSendResponse,
            use_user_token=True,
        )

    async def get_sms_status(
        self,
        request_model: DeliveryStatusRequest,
    ) -> DeliveryStatusResponse:
        '''
        Получение статусов сообщений.

        Args:
            request_model (DeliveryStatusRequest): Модель данных запроса для проверки статусов.

        Returns:
            DeliveryStatusResponse: Модель ответа с данными о статусах отправленных сообщений.

        Raises:
            ValidationError: Если ответ не соответствует ожидаемой модели.
            APIError: Если произошла ошибка при выполнении запроса.
        '''
        endpoint = '/delivery/status'

        return await self.request_and_parse(
            method=HTTPMethod.POST,
            endpoint=endpoint,
            request_model=request_model,
            response_model=DeliveryStatusResponse,
            use_user_token=True,
        )
