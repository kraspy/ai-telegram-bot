from datetime import date as d
from typing import Literal
from pydantic import BaseModel, Field


class TimeSlot(BaseModel):
    from_time: str = Field(
        default=...,
        pattern=r'^\d{2}:\d{2}:\d{2}$',
        description='Начало интервала',
    )
    to_time: str = Field(
        default=...,
        pattern=r'^\d{2}:\d{2}:\d{2}$',
        description='Конец интервала',
    )


class BusyInterval(BaseModel):
    entity_type: Literal['record', 'activity'] = Field(
        default=...,
        description='Тип сущности',
    )
    entity_id: int = Field(
        default=...,
        ge=1,
        description='Идентификатор сущности',
    )
    from_time: str = Field(
        default=...,
        pattern=r'^\d{2}:\d{2}:\d{2}$',
        description='Начало интервала',
    )
    to_time: str = Field(
        default=...,
        pattern=r'^\d{2}:\d{2}:\d{2}$',
        description='Конец интервала',
    )


class StaffScheduleData(BaseModel):
    staff_id: int = Field(
        default=...,
        ge=1,
        description='Идентификатор сотрудника',
    )
    date: d = Field(
        default=...,
        pattern=r'^\d{4}-\d{2}-\d{2}$',
        description='Дата расписания',
    )
    slots: list[TimeSlot] = Field(
        default=...,
        description='Массив интервалов работы сотрудника',
    )
    busy_intervals: list[BusyInterval] | None = Field(
        default=None,
        description='Занятые интервалы',
    )
    off_day_type: int | None = Field(
        default=None,
        description='Тип нерабочего дня',
    )


class Meta(BaseModel):
    count: int = Field(
        default=...,
        description='Количество объектов',
    )


class DeleteSchedule(BaseModel):
    staff_id: int = Field(
        default=...,
        description='ID сотрудника',
    )
    date: d = Field(
        default=...,
        description='Дата для удаления графика работы сотрудника в формате Y-m-d',
    )
