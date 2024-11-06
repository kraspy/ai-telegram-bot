from pydantic import Field
from ...common.models import BaseRequestModel, BaseQueryParamsModel, BaseBodyModel
from ._additional import NewTransaction, GoodsTransaction, Service

########################################################################################################################
# region Получить визит


class GetVisitQueryParams(BaseQueryParamsModel):
    '''
    Модель query-параметров для получения визита.

    Аргументы:
    - visit_id: Идентификатор визита.
    '''

    visit_id: int = Field(
        default=...,
        description='Идентификатор визита',
    )


class GetVisitRequest(BaseRequestModel):
    '''
    Модель запроса для получения визита.

    Аргументы:
    - query: Query-параметры для получения визита.
    '''

    query: GetVisitQueryParams | None = Field(default=None, description='Query-параметры запроса')


# endregion


########################################################################################################################
# region Получить детали визита


class GetVisitDetailsRequest(BaseRequestModel):
    '''
    Модель запроса для получения деталей визита.
    '''


# endregion


########################################################################################################################
# region Изменить визит


class UpdateVisitBodyParams(BaseBodyModel):
    '''
    Модель тела запроса для изменения визита.

    Аргументы:
    - attendance: Статус визита.
    - comment: Комментарий к визиту.
    - new_transactions: Список новых финансовых транзакций (опционально).
    - deleted_transaction_ids: Список ID удаленных транзакций (опционально).
    - goods_transactions: Список товарных транзакций (опционально).
    - services: Список услуг (опционально).
    - fast_payment: Способ быстрой оплаты (опционально).
    '''

    attendance: int = Field(
        default=...,
        description='Статус визита',
    )
    comment: str = Field(
        default=...,
        description='Комментарий',
    )
    new_transactions: list[NewTransaction] | None = Field(
        default=None,
        description='Новые финансовые транзакции',
    )
    deleted_transaction_ids: list[int] | None = Field(
        default=None,
        description='ID удаленных транзакций',
    )
    goods_transactions: list[GoodsTransaction] | None = Field(
        default=None,
        description='Товарные транзакции',
    )
    services: list[Service] | None = Field(
        default=None,
        description='Услуги',
    )
    fast_payment: int | None = Field(
        default=None,
        description='Быстрая оплата: 1 - наличные, 2 - безналичные, 129 - наличные с чеком, 130 - безналичные с чеком',
    )


class UpdateVisitRequest(BaseRequestModel):
    '''
    Модель запроса для изменения визита.

    Аргументы:
    - body: Тело запроса для изменения визита.
    '''

    body: UpdateVisitBodyParams = Field(
        default=...,
        description='Тело запроса для изменения визита',
    )


# endregion
