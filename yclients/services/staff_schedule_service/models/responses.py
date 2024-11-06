from pydantic import Field
from ...common.models import BaseResponseModel
from ._additional import StaffScheduleData, Meta

########################################################################################################################
# region Получение графиков работы сотрудников


class GetStaffScheduleResponse(BaseResponseModel):
    '''
    Модель ответа для получения графиков работы сотрудников.

    Аргументы:
    - success: Статус успешности выполнения запроса.
    - data: Массив графиков работы сотрудников.
    - meta: Дополнительная информация о запросе.
    '''

    success: bool = Field(
        default=...,
        description='Статус успешности выполнения запроса',
    )
    data: list[StaffScheduleData] = Field(
        default=...,
        description='Массив графиков работы сотрудников',
    )
    meta: Meta = Field(
        default=...,
        description='Дополнительная информация о запросе',
    )


# endregion


########################################################################################################################
# region Установка графиков работы сотрудников


class UpdateStaffScheduleResponse(BaseResponseModel):
    '''
    Модель ответа для установки графиков работы сотрудников.

    Аргументы:
    - success: Статус успешности выполнения запроса.
    - data: Массив обновленных графиков.
    - meta: Дополнительная информация о запросе.
    '''

    success: bool = Field(
        default=...,
        description='Статус успешности выполнения запроса',
    )
    data: list[StaffScheduleData] = Field(
        default=...,
        description='Массив обновленных графиков',
    )
    meta: Meta = Field(
        default=...,
        description='Дополнительная информация о запросе',
    )


# endregion
