from pydantic import Field
from ...common.models import BaseResponseModel
from ._additional import GetRecordData, Record, RecordPartner

########################################################################################################################
# region Получить список записей


class GetRecordsResponse(BaseResponseModel):
    '''
    Модель ответа для получения списка записей.

    Аргументы:
    - success: Статус успешности выполнения запроса.
    - data: Список записей.
    - meta: Дополнительные метаданные.
    '''

    success: bool = Field(
        default=...,
        description='Статус успешности выполнения запроса',
    )
    data: list[Record] = Field(
        default=...,
        description='Список записей',
    )
    meta: dict = Field(
        default=...,
        description='Дополнительные метаданные',
    )


# endregion


########################################################################################################################
# region Создать новую запись


class CreateRecordResponse(BaseResponseModel):
    '''
    Модель ответа для создания новой записи.

    Аргументы:
    - success: Статус успешности выполнения запроса.
    - data: Созданная запись.
    '''

    success: bool = Field(
        default=...,
        description='Статус успешности выполнения запроса',
    )
    data: Record = Field(
        default=...,
        description='Созданная запись',
    )


# endregion


########################################################################################################################
# region Получить список записей партнёра


class GetPartnerRecordsResponse(BaseResponseModel):
    '''
    Модель ответа для получения списка записей партнёра.

    Аргументы:
    - success: Статус успешности выполнения запроса.
    - data: Список записей партнёра.
    - meta: Дополнительная информация о запросе.
    '''

    success: bool = Field(
        default=...,
        description='Статус успешности выполнения запроса',
    )
    data: list[RecordPartner] = Field(
        default=...,
        description='Список записей партнера',
    )
    meta: dict = Field(
        default=...,
        description='Дополнительная информация о запросе',
    )


# endregion


########################################################################################################################
# region Получить запись


class GetRecordResponse(BaseResponseModel):
    '''
    Модель ответа для получения данных о записи.

    Аргументы:
    - success: Статус успешности выполнения запроса.
    - data: Данные записи.
    - meta: Метаданные (обычно пустые).
    '''

    success: bool = Field(
        default=...,
        description='Статус успешности выполнения запроса',
    )
    data: GetRecordData = Field(
        default=...,
        description='Данные записи',
    )
    meta: list[dict] = Field(
        default=...,
        description='Метаданные (обычно пустые)',
    )


# endregion


########################################################################################################################
# region Изменить запись


class UpdateRecordResponse(BaseResponseModel):
    '''
    Модель ответа для изменения записи.

    Аргументы:
    - success: Статус успешности выполнения запроса.
    - data: Обновленные данные записи.
    - meta: Метаданные (обычно пустые).
    '''

    success: bool = Field(
        default=...,
        description='Статус успешности выполнения запроса',
    )
    data: GetRecordData = Field(
        default=...,
        description='Обновленные данные записи',
    )
    meta: list[dict] = Field(
        default=...,
        description='Метаданные',
    )


# endregion


########################################################################################################################
# region Удалить запись


class DeleteRecordResponse(BaseResponseModel):
    '''
    Модель ответа для удаления записи.
    '''

    pass
