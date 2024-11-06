from pydantic import Field
from datetime import date as d
from ...common.models import BaseResponseModel
from ._additional import JournalSeance

########################################################################################################################
# region Журнал


class JournalDatesResponse(BaseResponseModel):
    '''
    Модель ответа для получения списка рабочих дат в журнале.

    Аргументы:
    - success: Статус успешности выполнения запроса.
    - data: Список рабочих дат.
    - meta: Метаданные запроса (по умолчанию пустой словарь).
    '''

    success: bool = Field(
        default=...,
        description='Статус успешности выполнения запроса',
    )
    data: list[d] = Field(
        default=...,
        description='Список рабочих дат',
    )
    meta: dict | None = Field(
        default=dict,
        description='Метаданные запроса',
    )


class JournalSeancesResponse(BaseResponseModel):
    '''
    Модель ответа для получения списка сеансов в журнале.

    Аргументы:
    - success: Статус успешности выполнения запроса.
    - data: Список сеансов.
    - meta: Метаданные запроса (по умолчанию пустой словарь).
    '''

    success: bool = Field(
        default=...,
        description='Статус успешности выполнения запроса',
    )
    data: list[JournalSeance] = Field(
        default=...,
        description='Список сеансов',
    )
    meta: dict | None = Field(
        default=dict,
        description='Метаданные запроса',
    )


# endregion
