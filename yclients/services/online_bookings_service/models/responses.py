from pydantic import Field
from ...common.models import BaseResponseModel
from ._additional import (
    BookServicesResponseData,
    BookableDatesData,
    Seance,
    BookRecordData,
    AppointmentError,
    RescheduleRecordData,
)

########################################################################################################################
# region Список доступных услуг


class BookableServicesResponse(BaseResponseModel):
    '''
    Модель ответа для получения списка доступных услуг.

    Аргументы:
    - success: Статус успешности выполнения запроса.
    - data: Объект с данными об услугах.
    - meta: Пустой массив для метаданных.
    '''

    success: bool = Field(
        default=...,
        description='Статус успешности выполнения запроса',
    )
    data: BookServicesResponseData = Field(
        default=...,
        description='Объект с данными',
    )
    meta: list = Field(
        default=list,
        description='Метаданные (пустой массив)',
    )


# endregion


########################################################################################################################
# region Список доступных дат


class BookableDatesResponse(BaseResponseModel):
    '''
    Модель ответа для получения списка доступных дат.

    Аргументы:
    - success: Статус успешности выполнения запроса.
    - data: Данные о доступных датах.
    - meta: Пустой массив для метаданных.
    '''

    success: bool = Field(
        default=...,
        description='Статус успешности выполнения запроса',
    )
    data: BookableDatesData = Field(
        default=...,
        description='Данные (объект)',
    )
    meta: list = Field(
        default=list,
        description='Метаданные (пустой массив)',
    )


# endregion


########################################################################################################################
# region Список доступных сеансов


class BookableTimesResponse(BaseResponseModel):
    '''
    Модель ответа для получения списка доступных сеансов.

    Аргументы:
    - success: Статус успешности выполнения запроса.
    - data: Список объектов с сеансами.
    - meta: Пустой массив для метаданных.
    '''

    success: bool = Field(
        default=...,
        description='Статус успешности выполнения запроса',
    )
    data: list[Seance] = Field(
        default=...,
        description='Массив объектов с данными',
    )
    meta: list = Field(
        default=list,
        description='Метаданные (пустой массив)',
    )


# endregion


########################################################################################################################
# region Создание записи на сеанс


class BookRecordResponse(BaseResponseModel):
    '''
    Модель ответа для создания записи на сеанс.

    Аргументы:
    - success: Статус успешности выполнения запроса.
    - data: Данные записи.
    - meta: Пустой массив или None.
    '''

    success: bool = Field(
        default=...,
        description='Статус успешности выполнения запроса',
    )
    data: list[BookRecordData] = Field(
        default=...,
        description='Данные записи',
    )
    meta: list | None = Field(
        default=None,
        description='Метаданные (пустой массив или None)',
    )


# endregion


########################################################################################################################
# region Проверка параметров записи


class CheckAppointmentsResponse(BaseResponseModel):
    '''
    Модель ответа для проверки параметров записи.

    Аргументы:
    - success: Статус успешности выполнения запроса.
    - meta: Пустой объект или None.
    - message: Сообщение с результатом проверки (опционально).
    - errors: Список ошибок, если они есть (опционально).
    '''

    success: bool = Field(
        default=...,
        description='Статус успешности выполнения запроса',
    )
    meta: dict | None = Field(
        default=None,
        description='Метаданные (пустой объект или None)',
    )
    message: str | None = Field(
        default=None,
        description='Сообщение с результатом проверки',
    )
    errors: list[AppointmentError] | None = Field(
        default=None,
        description='Список ошибок',
    )


# endregion


########################################################################################################################
# region Перенос записи на другой сеанс


class RescheduleRecordResponse(BaseResponseModel):
    '''
    Модель ответа для переноса записи на другой сеанс.

    Аргументы:
    - success: Статус успешности выполнения запроса.
    - data: Данные о перенесенной записи.
    - meta: Пустой объект или None.
    '''

    success: bool = Field(
        default=...,
        description='Статус успешности выполнения запроса',
    )
    data: RescheduleRecordData = Field(
        default=...,
        description='Данные перенесенной записи',
    )
    meta: dict | None = Field(
        default=None,
        description='Метаданные (пустой объект или None)',
    )


# endregion
