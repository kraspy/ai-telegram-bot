from pydantic import Field
from ...common.models import BaseRequestModel, BaseBodyModel

########################################################################################################################
# Авторизоваться по номеру телефона и коду


class UserAuthBodyParams(BaseBodyModel):
    '''
    Модель тела запроса для авторизации пользователя по номеру телефона или Email.

    Аргументы:
    - login: Номер телефона или Email пользователя.
    - password: Пароль пользователя.
    '''

    login: str = Field(
        default=...,
        description='Номер телефона или Email',
    )
    password: str = Field(
        default=...,
        description='Пароль',
    )


class UserAuthRequest(BaseRequestModel):
    '''
    Модель запроса для авторизации пользователя по номеру телефона и коду.

    Аргументы:
    - body: Тело запроса с параметрами для авторизации.
    '''

    body: UserAuthBodyParams = Field(
        default=...,
        description='Тело запроса для авторизации по номеру телефона и коду',
    )


# endregion


########################################################################################################################
# Получить записи пользователя


class UserRecordsRequest(BaseRequestModel):
    '''
    Модель запроса для получения записей пользователя.
    '''


# endregion


########################################################################################################################
# Удалить запись пользователя


class DeleteUserRecordRequest(BaseRequestModel):
    '''
    Модель запроса для удаления записи пользователя.
    '''

    pass


# endregion
