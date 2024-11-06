from pydantic import Field
from ...common.models import BaseResponseModel, DefaultResponse
from ._additional import (
    GetClientsResponseData,
    ClientResponseData,
    GetClientsResponseMeta,
    BulkCreateClientsResponseData,
    VisitsSearchResponseData,
    ClientComment,
    GetClientCommentsResponseMeta,
)


########################################################################################################################
# region Получить список клиентов
class GetClientsResponse(DefaultResponse):
    '''
    Модель ответа для получения списка клиентов.

    Аргументы:
    - data: Список данных клиентов.
    - meta: Метаданные (информация о количестве найденных клиентов).
    '''

    data: list[GetClientsResponseData] = Field(default=...)
    meta: GetClientsResponseMeta = Field(default=...)


# endregion


########################################################################################################################
# region CRUD клиента


class CreateClientResponse(DefaultResponse):
    '''
    Модель ответа для создания клиента.

    Аргументы:
    - data: Данные клиента.
    '''

    data: ClientResponseData = Field(default=...)


class GetClientResponse(DefaultResponse):
    '''
    Модель ответа для получения клиента.

    Аргументы:
    - data: Данные клиента.
    '''

    data: ClientResponseData = Field(default=...)


class UpdateClientResponse(BaseResponseModel):
    '''
    Модель ответа для изменения клиента.

    Аргументы:
    - data: Данные клиента.
    '''

    data: ClientResponseData = Field(default=...)


class DeleteClientResponse(BaseResponseModel):
    '''
    Модель ответа для удаления клиента.
    '''


# endregion


########################################################################################################################
# region Массовое добавление клиентов


class BulkCreateClientsResponse(DefaultResponse):
    '''
    Модель ответа для массового добавления клиентов.

    Аргументы:
    - data: Объект, содержащий списки успешно добавленных клиентов (created) и ошибки (errors).
    '''

    data: BulkCreateClientsResponseData


# endregion


########################################################################################################################
# region Поиск по Истории посещений клиента


class VisitsSearchResponse(BaseResponseModel):
    '''
    Модель ответа для поиска по истории посещений клиента.

    Аргументы:
    - data: Данные по визитам клиента, включая записи и продажи товаров.
    - meta: Объект информации о постраничной навигации, основанной на дате.
    '''

    data: VisitsSearchResponseData
    meta: dict  # TODO: Тут можно доработать (см. документацию YClients)


# endregion


########################################################################################################################
# region CRUD комментариев к клиенту


class GetClientCommentsResponse(DefaultResponse):
    '''
    Модель ответа для получения списка комментариев клиента.

    Аргументы:
    - data: Список комментариев клиента.
    - meta: Дополнительная информация о запросе.
    '''

    data: list[ClientComment]
    meta: GetClientCommentsResponseMeta = Field(default=...)


class CreateClientCommentResponse(BaseResponseModel):
    '''
    Модель ответа для добавления комментария к клиенту.

    Аргументы:
    - data: Созданный комментарий.
    - meta: Дополнительная информация о запросе (Пустой объект).
    '''

    data: ClientComment
    meta: dict = {}


class DeleteClientCommentResponse(BaseResponseModel):
    '''
    Модель ответа для удаления комментария клиента.

    Аргументы:
    - data: None, так как комментарий был удалён.
    - meta: Дополнительная информация о запросе (Пустой объект).
    '''

    success: bool = True
    data: None
    meta: dict = {}


# endregion
