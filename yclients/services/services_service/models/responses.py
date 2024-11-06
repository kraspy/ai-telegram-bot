from pydantic import Field
from ...common.models import BaseResponseModel
from ._additional import ServiceModel

########################################################################################################################
# region Получить список услуг / конкретную услугу


class ServicesResponse(BaseResponseModel):
    '''
    Модель ответа для получения списка услуг или конкретной услуги.

    Аргументы:
    - success: Статус успешности выполнения запроса.
    - data: Список услуг или данные конкретной услуги.
    - meta: Дополнительные метаданные.
    '''

    success: bool = Field(
        default=...,
        description='Статус успешности выполнения запроса',
    )
    data: list[ServiceModel] | dict = Field(
        default=...,
        description='Список услуг или данные конкретной услуги',
    )
    meta: dict | list = Field(
        default=...,
        description='Дополнительные метаданные',
    )


# endregion
