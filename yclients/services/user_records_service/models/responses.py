from pydantic import Field
from typing import Any
from ...common.models import BaseResponseModel
from ._additional import Record

########################################################################################################################
# Авторизоваться по номеру телефона и коду


class UserAuthResponse(BaseResponseModel):
    '''
    Модель ответа для авторизации пользователя по номеру телефона или Email.

    Аргументы:
    - user_token: Токен пользователя, полученный после успешной авторизации.
    '''

    user_token: str = Field(
        default=...,
        description='User_token пользователя',
    )


# endregion


########################################################################################################################
# Получить записи пользователя


class UserRecordsResponse(BaseResponseModel):
    '''
    Модель ответа для получения записей пользователя.

    Аргументы:
    - success: Статус успешности выполнения запроса.
    - data: Массив записей пользователя.
    - meta: Дополнительные метаданные (обычно пустой массив).
    '''

    success: bool = Field(
        default=...,
        description='Статус успешности выполнения запроса',
    )
    data: list[Record] = Field(
        default=...,
        description='Массив записей пользователя',
    )
    meta: list[Any] = Field(
        default=list,
        description='Метаданные (пустой массив)',
    )


# endregion


########################################################################################################################
# Удалить запись пользователя


class DeleteUserRecordResponse(BaseResponseModel):
    '''
    Модель ответа для удаления записи пользователя.
    '''

    pass
