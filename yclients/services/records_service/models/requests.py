from pydantic import Field
from datetime import datetime as dt
from ...common.models import BaseQueryParamsModel, BaseRequestModel, BaseBodyModel
from ._additional import ServiceCreate, ServiceUpdate, ClientCreate, ClientUpdate

########################################################################################################################
# region Получить список записей


class GetRecordsQueryParams(BaseQueryParamsModel):
    '''
    Модель query-параметров для получения списка записей.

    Аргументы:
    - staff_id: Идентификатор сотрудника (опционально).
    '''

    staff_id: int | None = Field(
        default=None,
        description='Идентификатор сотрудника (необязательно)',
    )


class GetRecordsRequest(BaseRequestModel):
    '''
    Модель запроса для получения списка записей.

    Аргументы:
    - query: Query-параметры запроса.
    '''

    query: GetRecordsQueryParams | None = Field(
        default=None,
        description='Query-параметры запроса',
    )


# endregion


########################################################################################################################
# region Создать новую запись


class CreateRecordBodyParams(BaseBodyModel):
    '''
    Модель тела запроса для создания новой записи.

    Аргументы:
    - staff_id: Идентификатор сотрудника.
    - services: Список услуг в записи.
    - client: Данные клиента.
    - datetime: Дата и время записи.
    - seance_length: Длительность сеанса в секундах.
    - send_sms: Отправлять ли SMS клиенту (опционально).
    - comment: Комментарий к записи (опционально).
    '''

    staff_id: int = Field(
        default=...,
        description='Идентификатор сотрудника',
    )
    services: list[ServiceCreate] = Field(
        default=...,
        description='Список услуг в записи',
    )
    client: ClientCreate = Field(
        default=...,
        description='Данные клиента',
    )
    datetime: dt = Field(
        default=...,
        description='Дата и время записи',
    )
    seance_length: int = Field(
        default=...,
        description='Длительность сеанса в секундах',
    )
    send_sms: bool | None = Field(
        default=None,
        description='Отправлять ли SMS клиенту',
    )
    comment: str | None = Field(
        default=None,
        description='Комментарий к записи',
    )


class CreateRecordRequest(BaseRequestModel):
    '''
    Модель запроса для создания новой записи.
    '''

    body: CreateRecordBodyParams = Field(
        default=...,
        description='Тело запроса для создания новой записи',
    )


# endregion


########################################################################################################################
# region Получить список записей партнёра


class GetPartnerRecordsQueryParams(BaseQueryParamsModel):
    '''
    Модель query-параметров для получения списка записей партнёра.

    Аргументы:
    - partner_id: Идентификатор партнера (опционально).
    '''

    partner_id: int | None = Field(
        default=None,
        description='Идентификатор партнера',
    )


class GetPartnerRecordsRequest(BaseRequestModel):
    '''
    Модель запроса для получения списка записей партнёра.
    '''

    query: GetPartnerRecordsQueryParams | None = Field(
        default=None,
        description='Query-параметры запроса',
    )


# endregion


########################################################################################################################
# region Получить запись


class GetRecordQueryParams(BaseQueryParamsModel):
    '''
    Модель query-параметров для получения данных о записи.

    Аргументы:
    - record_id: Идентификатор записи.
    '''

    record_id: int = Field(
        default=...,
        description='Идентификатор записи',
    )


class GetRecordRequest(BaseRequestModel):
    '''
    Модель запроса для получения данных о записи.
    '''

    query: GetRecordQueryParams | None = Field(
        default=None,
        description='Query-параметры запроса',
    )


# endregion


########################################################################################################################
# region Изменить запись


class UpdateRecordBodyParams(BaseBodyModel):
    '''
    Модель тела запроса для изменения записи.

    Аргументы:
    - staff_id: Идентификатор сотрудника (опционально).
    - services: Массив с изменёнными услугами (опционально).
    - client: Информация о клиенте (опционально).
    - datetime: Дата и время записи (опционально).
    - seance_length: Длительность записи в секундах (опционально).
    - comment: Комментарий к записи (опционально).
    - sms_remain_hours: Часы до визита для отправки SMS напоминания (опционально).
    - email_remain_hours: Часы до визита для отправки Email напоминания (опционально).
    - attendance: Статус записи (0 - ожидание, 1 - пришел, -1 - не пришел) (опционально).
    - custom_color: Цвет записи (опционально).
    - record_labels: Массив идентификаторов категорий записи (опционально).
    - custom_fields: Дополнительные поля записи (опционально).
    '''

    staff_id: int | None = Field(
        default=None,
        description='Идентификатор сотрудника',
    )
    services: list['ServiceUpdate'] | None = Field(
        default=None,
        description='Массив с измененными услугами',
    )
    client: ClientUpdate | None = Field(
        default=None,
        description='Информация о клиенте',
    )
    datetime: dt | None = Field(
        default=None,
        description='Дата и время записи',
    )
    seance_length: int | None = Field(
        default=None,
        description='Длительность записи в секундах',
    )
    comment: str | None = Field(
        default=None,
        description='Комментарий к записи',
    )
    sms_remain_hours: int | None = Field(
        default=None,
        description='Часы до визита для отправки SMS напоминания',
    )
    email_remain_hours: int | None = Field(
        default=None,
        description='Часы до визита для отправки Email напоминания',
    )
    attendance: int | None = Field(
        default=None,
        description='Статус записи (0 - ожидание, 1 - пришел, -1 - не пришел)',
    )
    custom_color: str | None = Field(
        default=None,
        description='Цвет записи',
    )
    record_labels: list[str] | None = Field(
        default=None,
        description='Массив идентификаторов категорий записи',
    )
    custom_fields: dict | None = Field(
        default=None,
        description='Дополнительные поля записи',
    )


class UpdateRecordRequest(BaseRequestModel):
    '''
    Модель запроса для изменения записи.
    '''

    body: UpdateRecordBodyParams = Field(
        default=...,
        description='Тело запроса для изменения записи',
    )


# endregion


########################################################################################################################
# region Удалить запись
class DeleteRecordRequest(BaseRequestModel):
    '''
    Модель запроса для удаления записи.
    '''

    pass
