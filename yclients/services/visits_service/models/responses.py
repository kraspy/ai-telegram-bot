from pydantic import Field
from ...common.models import BaseResponseModel
from ._additional import VisitResponseData, VisitDetailsData

########################################################################################################################
# region Получить визит


class GetVisitResponse(BaseResponseModel):
    '''
    Модель ответа для получения визита.

    Аргументы:
    - success: Статус успешности выполнения запроса.
    - data: Данные визита.
    - meta: Дополнительная информация.
    '''

    success: bool = Field(
        default=...,
        description='Статус успешности выполнения запроса',
    )
    data: VisitResponseData = Field(
        default=...,
        description='Данные визита',
    )
    meta: list[dict] = Field(
        default=...,
        description='Метаданные',
    )


# endregion


########################################################################################################################
# region Получить детали визита


class GetVisitDetailsResponse(BaseResponseModel):
    '''
    Модель ответа для получения деталей визита.

    Аргументы:
    - success: Статус успешности выполнения запроса.
    - data: Детали визита.
    - meta: Дополнительная информация.
    '''

    success: bool = Field(
        default=...,
        description='Статус успешности выполнения запроса',
    )
    data: VisitDetailsData = Field(
        default=...,
        description='Детали визита',
    )
    meta: list[dict] = Field(
        default=...,
        description='Метаданные',
    )


# endregion


########################################################################################################################
# region Изменить визит


class UpdateVisitResponse(BaseResponseModel):
    '''
    Модель ответа для изменения визита.

    Аргументы:
    - success: Статус успешности выполнения запроса.
    - data: Детали визита.
    - meta: Дополнительная информация.
    '''

    success: bool = Field(
        default=...,
        description='Статус успешности выполнения запроса',
    )
    data: VisitResponseData = Field(
        default=...,
        description='Детали визита',
    )
    meta: list[dict] = Field(
        default=...,
        description='Метаданные',
    )


# endregion
