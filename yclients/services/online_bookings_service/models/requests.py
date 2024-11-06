from typing import Any
from pydantic import Field
from datetime import datetime as dt, date as d
from ...common.models import BaseRequestModel, BaseQueryParamsModel, BaseBodyModel
from ._additional import Appointment

########################################################################################################################
# region Список доступных услуг


class BookableServicesQueryParams(BaseQueryParamsModel):
    '''
    Модель query-параметров для получения списка доступных услуг.

    Аргументы:
    - staff_id: ID сотрудника (опционально).
    - datetime: Дата и время услуги (опционально).
    - service_ids: Список ID услуг (опционально).
    '''

    staff_id: int | None = None
    datetime: dt | None = None
    service_ids: list[int] | None = None


class BookableServicesRequest(BaseRequestModel):
    '''
    Модель запроса для получения списка доступных услуг.

    Аргументы:
    - query: Query-параметры запроса.
    '''

    query: BookableServicesQueryParams | None = Field(
        default=None,
        description='Query-параметры запроса',
    )


# endregion


########################################################################################################################
# region Список доступных дат


class BookableDatesQueryParams(BaseQueryParamsModel):
    '''
    Модель query-параметров для получения доступных дат.

    Аргументы:
    - staff_id: ID сотрудника (опционально).
    - date: Конкретная дата (опционально).
    - date_from: Начальная дата диапазона (опционально).
    - date_to: Конечная дата диапазона (опционально).
    - service_ids: Список ID услуг (опционально).
    '''

    staff_id: int | None = None
    date: d | None = None
    date_from: str | None = None
    date_to: str | None = None
    service_ids: list[int] | None = None


class BookableDatesRequest(BaseRequestModel):
    '''
    Модель запроса для получения списка доступных дат.

    Аргументы:
    - query: Query-параметры запроса.
    '''

    query: BookableDatesQueryParams | None = Field(
        default=None,
        description='Query-параметры запроса',
    )


# endregion


########################################################################################################################
# region Список доступных сеансов


class BookableTimesQueryParams(BaseQueryParamsModel):
    '''
    Модель query-параметров для получения доступных сеансов.

    Аргументы:
    - service_ids: Список ID услуг (опционально).
    '''

    service_ids: list[int] | None = None


class BookableTimesRequest(BaseRequestModel):
    '''
    Модель запроса для получения списка доступных сеансов.

    Аргументы:
    - query: Query-параметры запроса.
    '''

    query: BookableTimesQueryParams | None = Field(
        default=None,
        description='Query-параметры запроса',
    )


# endregion


########################################################################################################################
# region Создание записи на сеанс


class BookRecordRequestBody(BaseBodyModel):
    '''
    Модель тела запроса для создания записи на сеанс.

    Аргументы:
    - phone: Телефон клиента.
    - fullname: Имя клиента.
    - email: Почтовый адрес клиента.
    - code: Код подтверждения (если требуется).
    - comment: Комментарий к записи (опционально).
    - type: Источник записи (опционально).
    - notify_by_sms: Количество часов до визита для SMS напоминания (опционально).
    - notify_by_email: Количество часов до визита для Email напоминания (опционально).
    - api_id: ID записи из внешней системы (опционально).
    - custom_fields: Дополнительные поля клиента (опционально).
    - appointments: Список параметров записей (сеанс, услуги, мастер).
    '''

    phone: str = Field(
        default=...,
        description='Телефон клиента',
    )
    fullname: str = Field(
        default=...,
        description='Имя клиента',
    )
    email: str = Field(
        default=...,
        description='Почтовый адрес клиента',
    )
    code: int | None = Field(
        default=None,
        description='Код подтверждения телефона, высланный по СМС (обязателен, если требуется)',
    )
    comment: str | None = Field(
        default=None,
        description='Комментарий к записи',
    )
    type: str | None = Field(
        default=None,
        description='Источник записи',
    )
    notify_by_sms: int | None = Field(
        default=None,
        description='За сколько часов до визита выслать СМС напоминание',
    )
    notify_by_email: int | None = Field(
        default=None,
        description='За сколько часов до визита выслать email напоминание',
    )
    api_id: int | None = Field(
        default=None,
        description='ID записи из внешней системы',
    )
    custom_fields: dict[str, Any] | None = Field(
        default=None,
        description='Дополнительные поля карточки клиента',
    )
    appointments: list[Appointment] = Field(
        default=...,
        description='Параметры записей (сеанс, услуги, мастер)',
    )


class BookRecordRequest(BaseRequestModel):
    '''
    Модель запроса для создания записи на сеанс.

    Аргументы:
    - body: Тело запроса с данными для записи.
    '''

    body: BookRecordRequestBody = Field(
        default=...,
        description='Тело запроса для создания записи',
    )


# endregion


########################################################################################################################
# region Проверка параметров записи


class CheckAppointmentsBodyParams(BaseBodyModel):
    '''
    Модель тела запроса для проверки параметров записи.

    Аргументы:
    - appointments: Список параметров записей (сеанс, услуги, мастер).
    '''

    appointments: list['Appointment'] = Field(
        default=...,
        description='Параметры записей для проверки',
    )


class CheckAppointmentsRequest(BaseRequestModel):
    '''
    Модель запроса для проверки параметров записи.

    Аргументы:
    - body: Тело запроса с параметрами записей.
    '''

    body: CheckAppointmentsBodyParams = Field(
        default=...,
        description='Тело запроса для проверки параметров записи',
    )


# endregion


########################################################################################################################
# region Перенос записи на другой сеанс


class RescheduleRecordBodyParams(BaseBodyModel):
    '''
    Модель тела запроса для переноса записи на другой сеанс.

    Аргументы:
    - datetime: Новая дата и время записи в формате ISO8601.
    - comment: Комментарий к переносу записи (опционально).
    '''

    datetime: dt = Field(
        default=...,
        description='Дата и время в формате ISO8601',
    )
    comment: str | None = Field(
        default=None,
        description='Комментарий к переносу записи',
    )


class RescheduleRecordRequest(BaseRequestModel):
    '''
    Модель запроса для переноса записи на другой сеанс.

    Аргументы:
    - body: Тело запроса с новыми параметрами записи.
    '''

    body: RescheduleRecordBodyParams = Field(
        default=...,
        description='Тело запроса для переноса записи',
    )


# endregion
