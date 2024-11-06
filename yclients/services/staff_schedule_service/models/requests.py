from datetime import datetime as d
from pydantic import Field
from typing import Literal
from ...common.models import BaseRequestModel, BaseQueryParamsModel, BaseBodyModel
from ._additional import StaffScheduleData, DeleteSchedule

########################################################################################################################
# region Получение графиков работы сотрудников


class GetStaffScheduleQueryParams(BaseQueryParamsModel):
    '''
    Модель query-параметров для получения графиков работы сотрудников.

    Аргументы:
    - start_date: Дата начала поиска расписаний сотрудников в формате Y-m-d (опционально).
    - end_date: Дата окончания поиска расписаний сотрудников в формате Y-m-d (опционально).
    - staff_ids: Набор идентификаторов сотрудников для поиска расписаний (опционально).
    - include: Сущности для включения в ответ (опционально).
    '''

    start_date: d | None = Field(
        default=None,
        pattern=r'^\d{4}-\d{2}-\d{2}$',
        description='Дата начала поиска расписаний сотрудников в формате Y-m-d',
    )
    end_date: d | None = Field(
        default=None,
        pattern=r'^\d{4}-\d{2}-\d{2}$',
        description='Дата окончания поиска расписаний сотрудников в формате Y-m-d',
    )
    staff_ids: list[int] | None = Field(
        default=None,
        ge=1,
        description='Набор идентификаторов сотрудников для поиска расписаний',
    )
    include: list[Literal['busy_intervals', 'off_day_type']] | None = Field(
        default=None,
        description='Сущности, которые должны быть включены в ответ',
    )


class GetStaffScheduleRequest(BaseRequestModel):
    '''
    Модель запроса для получения графиков работы сотрудников.

    Аргументы:
    - query: Query-параметры для получения графиков сотрудников.
    '''

    query: GetStaffScheduleQueryParams = Field(
        default=...,
        description='Query параметры для получения графиков работы сотрудников',
    )


# endregion


########################################################################################################################
# region Установка графиков работы сотрудников


class UpdateStaffScheduleBodyParams(BaseBodyModel):
    '''
    Модель тела запроса для установки графиков работы сотрудников.

    Аргументы:
    - schedules_to_set: Массив графиков для установки.
    - schedules_to_delete: Массив графиков для удаления (опционально).
    '''

    schedules_to_set: list[StaffScheduleData] = Field(
        default=...,
        description='Массив графиков для установки',
    )
    schedules_to_delete: list[DeleteSchedule] | None = Field(
        default=None,
        description='Массив графиков для удаления',
    )


class UpdateStaffScheduleRequest(BaseRequestModel):
    '''
    Модель запроса для установки графиков работы сотрудников.

    Аргументы:
    - body: Тело запроса с графиками для установки или удаления.
    '''

    body: UpdateStaffScheduleBodyParams = Field(
        default=...,
        description='Тело запроса для установки графиков работы сотрудников',
    )


# endregion
