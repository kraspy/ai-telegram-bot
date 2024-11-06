from datetime import datetime as dt
from datetime import date as d
from pydantic import Field, BaseModel

from ...common.models import (
    BaseMeta,
    BaseResponseData,
    BaseClient,
    BaseClientComment,
    BaseRecord,
    BaseTransaction,
    BaseCommentFile,
    BaseCommentUser,
)


# region Модели данных клиента


class ClientRequestData(BaseClient):
    '''Описание см. в модели BaseClient.'''

    surname: str | None = None
    patronymic: str | None = None
    email: str | None = None
    sex_id: int | None = None
    importance_id: int | None = None
    discount: float | None = None
    card: str | None = None
    birth_date: d | None = None
    comment: str | None = None
    spent: float | None = None
    balance: float | None = None
    sms_check: int | None = None
    sms_not: int | None = None
    categories: list[int] | None = None
    custom_fields: dict | None = None


class ClientResponseData(BaseResponseData):
    '''Описание см. в модели BaseClient.'''

    id: int = Field(default=..., description='ID клиента')
    sex: str = Field(default=..., description='Пол клиента')
    importance: str = Field(default=..., description='Статус важности клиента')
    visits: int = Field(default=..., description='Количество визитов клиента')
    last_change_date: dt = Field(default=..., description='Дата последнего изменения записи о клиенте')
    custom_fields: dict = Field(default=..., description='Дополнительные поля клиента')


class GetClientsResponseData(BaseResponseData):
    '''Описание см. в BaseClient.'''

    id: int
    name: str | None = None
    surname: str | None = None
    patronymic: str | None = None
    phone: str | None = None
    email: str | None = None
    categories: list[int] | None = None
    sex: str | None = None
    sex_id: int | None = None
    discount: float | None = None
    importance_id: int | None = None
    importance: str | None = None
    card: str | None = None
    birth_date: d | None = None
    comment: str | None = None
    sms_check: int | None = None
    sms_not: int | None = None
    spent: float | None = None
    balance: float | None = None
    visits: int | None = None
    last_change_date: dt | None = None
    custom_fields: dict | None = None


# endregion


# region Зависимости ответов для сервиса клиентов
class GetClientsResponseMeta(BaseMeta):
    '''
    Модель метаданных получения списка клиентов.

    Аргументы:
    - total_count: Количество найденных клиентов.
    '''

    total_count: int = Field(default=..., ge=0)


class GetClientCommentsResponseMeta(BaseMeta):
    '''
    Модель метаданных получения списка комментариев к клиенту.

    Аргументы:
    - count: Количество найденных клиентов.
    '''

    count: int = Field(default=..., ge=0)


class BulkCreateClientError(BaseModel):
    name: str | None = None
    phone: str | None = None
    surname: str | None = None
    patronymic: str | None = None
    email: str | None = None
    sex_id: int | None = None
    importance_id: int | None = None
    discount: float | None = None
    card: str | None = None
    birth_date: d | None = None
    comment: str | None = None
    spent: float | None = None
    balance: float | None = None
    sms_check: int | None = None
    sms_not: int | None = None
    categories: list[int] | None = None
    custom_fields: dict | None = None
    error: str = Field(
        default=...,
        description='Описание ошибки',
    )


class BulkCreateClientsResponseData(BaseResponseData):
    created: list[ClientResponseData] = Field(
        default=list,
        description='Список успешно созданных клиентов',
    )
    errors: list[BulkCreateClientError] = Field(
        default=list,
        description='Список ошибок при создании клиентов',
    )


class GoodsTransaction(BaseTransaction):
    pass


class Record(BaseRecord):
    pass


class VisitsSearchResponseData(BaseResponseData):
    goods_transactions: list[GoodsTransaction] = Field(
        default=...,
        description='Список транзакций по продажам товаров',
    )
    records: list[Record] = Field(
        default=...,
        description='Список записей клиента',
    )


class CommentFile(BaseCommentFile):
    pass


class CommentUser(BaseCommentUser):
    pass


class ClientComment(BaseClientComment):
    pass


# endregion
