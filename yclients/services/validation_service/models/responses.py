from pydantic import Field
from ...common.models import BaseResponseModel
from ._additional import ValidatePhoneResponseData

########################################################################################################################
# region Проверка формата номера телефона


class ValidatePhoneResponse(BaseResponseModel):
    '''
    Модель ответа для проверки формата номера телефона.

    Аргументы:
    - success: Статус успешности выполнения запроса.
    - data: Результаты проверки номера телефона.
    - meta: Дополнительная информация (обычно пустой массив).
    '''

    success: bool = Field(
        default=...,
        description='Успешность выполнения запроса',
    )
    data: ValidatePhoneResponseData = Field(
        default=...,
        description='Результаты проверки номера телефона',
    )
    meta: list = Field(
        default=[],
        description='Дополнительная информация',
    )


# endregion
