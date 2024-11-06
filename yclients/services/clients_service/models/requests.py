from datetime import date as d
from pydantic import Field, ConfigDict

from ._additional import ClientRequestData
from ...common.models import BaseClient, BaseRequestModel, BaseBodyModel
from ...common.enums import PaymentStatus

from .utils.get_clients_filter import (
    IDFilter,
    SoldAmountFilter,
    QuickSearchFilter,
    ImportanceFilter,
    HasMobileAppFilter,
    CategoryFilter,
    HasPassteamCardFilter,
    PassteamCardIDsFilter,
    BirthdayFilter,
    GenderFilter,
    RecordFilter,
    ClientFilter,
)

########################################################################################################################
# region Получить список клиентов


class GetClientsRequestBody(BaseBodyModel):
    '''
    Модель запроса для получения списка клиентов.

    Аргументы:
    - page: Номер страницы.
    - page_size: Количество выводимых строк на странице. Max: 200. Default: 25.
    - fields: Список полей для возврата в ответе.
    - order_by: Поле для сортировки.
    - order_by_direction: Направление сортировки (ASC/DESC).
    - operation: Логическая операция для фильтров (AND/OR).
    - filters: Список фильтров для применения.
    '''

    page: int | None = Field(default=None, description='Номер страницы')
    page_size: int | None = Field(
        default=None,
        description='Количество выводимых строк на странице. Max: 200. Default: 25',
    )
    fields: list[str] | None = Field(
        default=None,
        description='Поля, которые нужно вернуть в ответе',
    )
    order_by: str | None = Field(
        default=None,
        description='По какому полю сортировать',
        pattern='^(id|name|phone|email|discount|first_visit_date|last_visit_date|sold_amount|visits_count)$',
    )
    order_by_direction: str | None = Field(
        default=None,
        description='Как сортировать (по возрастанию / по убыванию)',
        pattern='^(ASC|DESC)$',
    )
    operation: str | None = Field(
        default=None,
        description='Тип операции',
        pattern='^(AND|OR)$',
    )
    filters: (
        list[
            IDFilter
            | SoldAmountFilter
            | QuickSearchFilter
            | ImportanceFilter
            | HasMobileAppFilter
            | CategoryFilter
            | HasPassteamCardFilter
            | PassteamCardIDsFilter
            | BirthdayFilter
            | GenderFilter
            | RecordFilter
            | ClientFilter
        ]
        | None
    ) = Field(default=None, description='Список фильтров')


class GetClientsRequest(BaseRequestModel):
    '''
    Модель запроса для получения списка клиентов.

    Аргументы:
    - body: Тело запроса, содержащее параметры фильтрации и сортировки.
    '''

    body: GetClientsRequestBody = Field(
        default=...,
        description='Body запроса',
    )
    query: None = None


# endregion


########################################################################################################################
# region CRUD клиента


class CreateClientsRequestBody(BaseClient, BaseBodyModel):
    pass


class CreateClientRequest(BaseRequestModel):
    '''
    Модель запроса для создания нового клиента.

    Аргументы:
    - body: Данные клиента для создания.
    '''

    body: CreateClientsRequestBody = Field(
        default=...,
        description='Body запроса',
    )


class GetClientRequest(BaseRequestModel):
    '''
    Модель запроса для получения информации о клиенте.
    '''

    pass


class UpdateClientRequest(BaseRequestModel):
    '''
    Модель запроса для обновления данных клиента.

    Аргументы:
    - body: Данные клиента для обновления.
    '''

    body: ClientRequestData = Field(
        default=...,
        description='Body запроса',
    )


class DeleteClientRequest(BaseRequestModel):
    '''
    Модель запроса для удаления клиента.
    '''

    pass


# endregion


########################################################################################################################
# region Массовое добавление клиентов
class BulkCreateClientsRequestBody(BaseBodyModel):
    clients: list[ClientRequestData]

    def model_dump(self, *args, **kwargs):
        data = super().model_dump(*args, **kwargs)
        return data['clients']


class BulkCreateClientsRequest(BaseRequestModel):
    '''
    Модель запроса для массового добавления клиентов.

    Аргументы:
    - body: Список данных клиентов для создания.
    '''

    body: BulkCreateClientsRequestBody = Field(default=..., description='Body запроса')


# endregion


########################################################################################################################
# region Поиск по Истории посещений клиента


class VisitsSearchRequestBody(BaseBodyModel):
    '''
    Модель запроса для поиска по истории посещений клиента.

    Аргументы:
    - client_id: ID клиента.
    - client_phone: Телефон клиента.
    - from_: Дата начала периода.
    - to: Дата конца периода.
    - payment_statuses: Список статусов оплаты.
    - attendance: Статус посещения.
    '''

    client_id: int | None = Field(default=None, description='ID клиента')
    client_phone: str | None = Field(default=None, description='Телефон клиента')
    from_date: d | None = Field(default=None, description='Дата начала периода', serialization_alias='from')
    to_date: d | None = Field(default=None, description='Дата конца периода', alias='to')
    payment_statuses: list[PaymentStatus] = Field(default=[], description='Статус оплаты визита.')
    attendance: int | None = Field(
        default=None,
        ge=-1,
        le=2,
        description='Статус посещения: -1 — не пришёл, 0 — ожидание, 1 — пришёл, 2 — подтвердил запись',
    )

    model_config = ConfigDict(populate_by_name=True)


class VisitsSearchRequest(BaseRequestModel):
    '''
    Модель запроса для поиска по истории посещений клиента.

    Аргументы:
    - body: Тело запроса, содержащее параметры поиска.
    '''

    body: VisitsSearchRequestBody = Field(
        default=...,
        description='Body запроса',
    )


# endregion


########################################################################################################################
# region CRUD комментариев к клиенту


class GetClientCommentsRequest(BaseRequestModel):
    '''
    Модель запроса для получения списка комментариев к клиенту.
    '''


class CreateClientCommentRequest(BaseRequestModel):
    '''
    Модель запроса для добавления комментария к клиенту.

    Аргументы:
    - body: Тело запроса с текстом комментария.
    '''

    body: BaseBodyModel = Field(
        default=...,
        description='Тело запроса.',
    )


class DeleteClientCommentRequest(BaseRequestModel):
    '''
    Модель запроса для удаления комментария к клиенту.
    '''


# endregion
