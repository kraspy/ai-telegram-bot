from pydantic import Field

from ...common.models import BaseResponseData


########################################################################################################################
# region Проверка формата номера телефона
class ValidatePhoneResponseData(BaseResponseData):
    is_valid: bool = Field(
        default=...,
        description='Статус проверки, является ли телефонный номер валидным',
    )


# endregion
