from pydantic import Field
from ...common.models import BaseRequestModel, BaseQueryParamsModel, BaseBodyModel
from ...common.enums import ShippingChannel


########################################################################################################################
# region SMS рассылка по списку клиентов


class SmsClientsByIdBodyParams(BaseBodyModel):
    '''
    Модель тела запроса для отправки SMS рассылки по списку клиентов.

    Аргументы:
    - client_ids: Массив идентификаторов клиентов.
    - text: Текст SMS сообщения.
    '''

    client_ids: list[int] = Field(
        default=...,
        description='Массив идентификаторов клиентов',
    )
    text: str = Field(
        default=...,
        description='Текст SMS сообщения',
    )


class SmsClientsByIdRequest(BaseRequestModel):
    '''
    Модель запроса для отправки SMS рассылки по списку клиентов.

    Аргументы:
    - body: Тело запроса с данными для отправки.
    '''

    body: SmsClientsByIdBodyParams = Field(
        default=...,
        description='Тело запроса для рассылки по списку клиентов',
    )


# endregion


########################################################################################################################
# region SMS рассылка по клиентам с фильтрами


class SmsClientsByFilterQueryParams(BaseQueryParamsModel):
    '''
    Модель query-параметров для фильтрации клиентов перед отправкой SMS.

    Аргументы:
    - fullname: Часть имени для фильтрации.
    - phone: Часть номера телефона для фильтрации.
    - email: Часть Email для фильтрации.
    - card: Часть карты лояльности для фильтрации.
    '''

    fullname: str | None = Field(
        default=None,
        description='Часть имени для фильтрации',
    )
    phone: str | None = Field(
        default=None,
        description='Часть номера телефона для фильтрации',
    )
    email: str | None = Field(
        default=None,
        description='Часть Email для фильтрации',
    )
    card: str | None = Field(
        default=None,
        description='Часть карты лояльности для фильтрации',
    )


class SmsClientsByFilterBodyParams(BaseBodyModel):
    '''
    Модель тела запроса для отправки SMS сообщения по фильтрованным клиентам.

    Аргументы:
    - text: Текст SMS сообщения.
    '''

    text: str = Field(
        default=...,
        description='Текст SMS сообщения',
    )


class SmsClientsByFilterRequest(BaseRequestModel):
    '''
    Модель запроса для отправки SMS сообщения по клиентам, подходящим под фильтры.

    Аргументы:
    - query: Query параметры фильтрации клиентов.
    - body: Тело запроса с данными для отправки.
    '''

    query: SmsClientsByFilterQueryParams = Field(
        default=...,
        description='Query параметры фильтрации клиентов',
    )
    body: SmsClientsByFilterBodyParams = Field(
        default=...,
        description='Тело запроса для рассылки по фильтрованным клиентам',
    )


# endregion


########################################################################################################################
# region Email рассылка по списку клиентов


class EmailClientsByIdBodyParams(BaseBodyModel):
    '''
    Модель тела запроса для отправки Email рассылки по списку клиентов.

    Аргументы:
    - client_ids: Массив идентификаторов клиентов.
    - subject: Тема Email сообщения.
    - text: Текст Email сообщения.
    '''

    client_ids: list[int] = Field(
        default=...,
        description='Массив идентификаторов клиентов',
    )
    subject: str = Field(
        default=...,
        description='Тема Email сообщения',
    )
    text: str = Field(
        default=...,
        description='Текст Email сообщения',
    )


class EmailClientsByIdRequest(BaseRequestModel):
    '''
    Модель запроса для отправки Email рассылки по списку клиентов.

    Аргументы:
    - body: Тело запроса с данными для отправки.
    '''

    body: EmailClientsByIdBodyParams = Field(
        default=...,
        description='Тело запроса для рассылки по списку клиентов',
    )


# endregion


########################################################################################################################
# region Email рассылка по клиентам с фильтрами


class EmailClientsByFilterQueryParams(BaseQueryParamsModel):
    '''
    Модель query-параметров для фильтрации клиентов перед отправкой Email.

    Аргументы:
    - fullname: Часть имени для фильтрации.
    - phone: Часть номера телефона для фильтрации.
    - email: Часть Email для фильтрации.
    - card: Часть карты лояльности для фильтрации.
    '''

    fullname: str | None = Field(
        default=None,
        description='Часть имени для фильтрации',
    )
    phone: str | None = Field(
        default=None,
        description='Часть номера телефона для фильтрации',
    )
    email: str | None = Field(
        default=None,
        description='Часть Email для фильтрации',
    )
    card: str | None = Field(
        default=None,
        description='Часть карты лояльности для фильтрации',
    )


class EmailClientsByFilterBodyParams(BaseBodyModel):
    '''
    Модель тела запроса для отправки Email сообщения по фильтрованным клиентам.

    Аргументы:
    - subject: Тема Email сообщения.
    - text: Текст Email сообщения.
    '''

    subject: str = Field(
        default=...,
        description='Тема Email сообщения',
    )
    text: str = Field(
        default=...,
        description='Текст Email сообщения',
    )


class EmailClientsByFilterRequest(BaseRequestModel):
    '''
    Модель запроса для отправки Email сообщения по клиентам, подходящим под фильтры.

    Аргументы:
    - query: Query параметры фильтрации клиентов.
    - body: Тело запроса с данными для отправки.
    '''

    query: EmailClientsByFilterQueryParams = Field(
        default=...,
        description='Query параметры фильтрации клиентов',
    )
    body: EmailClientsByFilterBodyParams = Field(
        default=...,
        description='Тело запроса для рассылки по фильтрованным клиентам',
    )


# endregion


########################################################################################################################
# region Отправка СМС


class SmsSendBodyParams(BaseBodyModel):
    '''
    Модель тела запроса для отправки индивидуального SMS сообщения.

    Аргументы:
    - destination_params: Параметры ID отправки и номера телефона.
    - from_: Имя отправителя.
    - text: Текст сообщения.
    - channel: Канал отправки (например, SMS).
    - dispatch_type: Тип рассылки (service - сервисная, adds - рекламная).
    - delivery_callback_url: URL для получения статуса сообщения.
    '''

    destination_params: dict[str, str] = Field(
        default=...,
        description='Параметры ID отправки и номера телефона',
    )
    from_: str = Field(
        default=...,
        alias='from',
        description='Имя отправителя',
    )
    text: str = Field(
        default=...,
        description='Текст сообщения',
    )
    channel: ShippingChannel = Field(
        default=...,
        description='Канал отправки',
    )
    dispatch_type: str = Field(
        default=...,
        description='Тип рассылки (service - сервисная, adds - рекламная)',
    )
    delivery_callback_url: str = Field(
        default=...,
        description='URL для получения статуса сообщения',
    )


class SmsSendRequest(BaseRequestModel):
    '''
    Модель запроса для отправки индивидуального SMS сообщения.

    Аргументы:
    - body: Тело запроса с данными для отправки.
    '''

    body: SmsSendBodyParams = Field(
        default=...,
        description='Тело запроса для отправки СМС',
    )


# endregion


########################################################################################################################
# region Получение статусов сообщений


class DeliveryStatusBodyParams(BaseBodyModel):
    '''
    Модель тела запроса для получения статуса сообщения.

    Аргументы:
    - id: Идентификатор сообщения.
    - status: Статус сообщения.
    - payment_sum: Полная стоимость сообщения.
    - currency_iso: ISO код валюты платежа.
    - parts_amount: Количество частей сообщения.
    '''

    id: str = Field(
        default=...,
        description='Идентификатор сообщения',
    )
    status: str = Field(
        default=...,
        description='Статус сообщения',
    )
    payment_sum: float = Field(
        default=...,
        description='Полная стоимость сообщения',
    )
    currency_iso: str = Field(
        default=...,
        description='ISO валюты платежа (например: RUB, EUR, BYN)',
    )
    parts_amount: int = Field(
        default=...,
        description='Количество частей сообщения',
    )


class DeliveryStatusRequest(BaseRequestModel):
    '''
    Модель запроса для получения статусов сообщений.

    Аргументы:
    - body: Список данных для проверки статусов сообщений.
    '''

    body: list[DeliveryStatusBodyParams] = Field(
        default=...,
        description='Тело запроса для получения статуса сообщения',
    )


# endregion
