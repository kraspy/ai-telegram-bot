from pydantic import Field
from datetime import date as d
from ...common.models import BaseRequestModel, BaseQueryParamsModel

########################################################################################################################
# region Журнал


class JournalDatesQueryParams(BaseQueryParamsModel):
    '''
    Модель query-параметров для запроса списка дат в журнале.

    Аргументы:
    - date: Дата в формате YYYY-MM-DD.
    - staff_id: ID сотрудника (опционально).
    '''

    date: d = Field(
        default=...,
        description='Дата в формате YYYY-MM-DD',
    )
    staff_id: int | None = Field(
        default=None,
        description='ID сотрудника',
    )


class JournalDatesRequest(BaseRequestModel):
    '''
    Модель запроса для получения списка дат в журнале.

    Аргументы:
    - query: Query-параметры запроса.
    '''

    query: JournalDatesQueryParams = Field(
        default=...,
        description='Query-параметры запроса',
    )


class JournalSeancesQueryParams(BaseQueryParamsModel):
    '''
    Модель query-параметров для запроса списка сеансов в журнале.

    Аргументы:
    - date: Дата сеансов в формате YYYY-MM-DD.
    - staff_id: ID сотрудника.
    '''

    date: d = Field(
        default=...,
        description='Дата в формате YYYY-MM-DD',
    )
    staff_id: int = Field(
        default=...,
        description='ID сотрудника',
    )


class JournalSeancesRequest(BaseRequestModel):
    '''
    Модель запроса для получения списка сеансов в журнале.

    Аргументы:
    - query: Query-параметры запроса.
    '''

    query: JournalSeancesQueryParams = Field(
        default=...,
        description='Query-параметры запроса',
    )


# endregion
