from pydantic import Field
from ...common.models import BaseResponseModel

########################################################################################################################
# region SMS рассылка по списку клиентов


class SmsClientsByIdResponse(BaseResponseModel):
    '''
    Модель ответа для отправки SMS рассылки по списку клиентов.

    Аргументы:
    - success: Статус успешности выполнения запроса.
    - meta: Сообщение об успешной отправке.
    '''

    success: bool = Field(
        default=...,
        description='Статус успешности выполнения запроса',
    )
    meta: dict = Field(
        default=...,
        description='Сообщение об успешной отправке',
    )


# endregion


########################################################################################################################
# region SMS рассылка по клиентам с фильтрами


class SmsClientsByFilterResponse(BaseResponseModel):
    '''
    Модель ответа для отправки SMS рассылки по фильтрованным клиентам.

    Аргументы:
    - success: Статус успешности выполнения запроса.
    - data: null, так как возвращаемых данных нет.
    - meta: Объект с сообщением 201 статус-кода.
    '''

    success: bool = Field(
        default=...,
        description='Статус успешности выполнения запроса',
    )
    data: None = Field(
        default=None,
        description='Данные ответа: null',
    )
    meta: dict = Field(
        default=dict,
        description='Объект, содержащий сообщение 201 статус-кода',
    )


# endregion


########################################################################################################################
# region Email рассылка по списку клиентов


class EmailClientsByIdResponse(BaseResponseModel):
    '''
    Модель ответа для отправки Email рассылки по списку клиентов.

    Аргументы:
    - success: Статус успешности выполнения запроса.
    - meta: Сообщение об успешной отправке.
    '''

    success: bool = Field(
        default=...,
        description='Статус успешности выполнения запроса',
    )
    meta: dict = Field(
        default=dict,
        description='Сообщение об успешной отправке',
    )


# endregion


########################################################################################################################
# region Email рассылка по клиентам с фильтрами


class EmailClientsByFilterResponse(BaseResponseModel):
    '''
    Модель ответа для отправки Email рассылки по фильтрованным клиентам.

    Аргументы:
    - success: Статус успешности выполнения запроса.
    - meta: Сообщение об успешной отправке.
    '''

    success: bool = Field(
        default=...,
        description='Статус успешности выполнения запроса',
    )
    meta: dict = Field(
        default=dict,
        description='Сообщение об успешной отправке',
    )


# endregion


########################################################################################################################
# region Отправка СМС


class SmsSendResponse(BaseResponseModel):
    '''
    Модель ответа для отправки индивидуального SMS сообщения.

    Аргументы:
    - id: Идентификатор записи.
    - ext_id: Внешний идентификатор (если успешен).
    - error_code: Код ошибки (если произошла ошибка).
    - error_message: Сообщение об ошибке (если произошла ошибка).
    '''

    id: str = Field(
        default=...,
        description='Идентификатор записи',
    )
    ext_id: str | None = Field(
        default=None,
        description='Внешний идентификатор, если запрос успешен',
    )
    error_code: int | None = Field(
        default=None,
        description='Код ошибки, если запрос завершился ошибкой',
    )
    error_message: str | None = Field(
        default=None,
        description='Сообщение об ошибке, если запрос завершился ошибкой',
    )


# endregion


########################################################################################################################
# region Получение статусов сообщений


class DeliveryStatusResponse(BaseResponseModel):
    '''
    Модель ответа для получения статусов сообщений.

    Аргументы:
    - success: Статус успешности выполнения запроса.
    '''

    success: bool = Field(
        default=...,
        description='Статус успешности выполнения запроса',
    )


# endregion
