from datetime import datetime as dt
from datetime import date as d
from pydantic import BaseModel, Field

from ...common.models import BaseResponseData


########################################################################################################################
# region Получить визит
class StaffPosition(BaseModel):
    id: int = Field(
        default=...,
        description='Идентификатор должности',
    )
    title: str = Field(
        default=...,
        description='Название должности',
    )


class Staff(BaseModel):
    id: int = Field(
        default=...,
        description='Идентификатор сотрудника',
    )
    name: str = Field(
        default=...,
        description='Имя сотрудника',
    )
    specialization: str | None = Field(
        default=None,
        description='Специализация сотрудника',
    )
    position: StaffPosition | None = Field(
        default=None,
        description='Должность сотрудника',
    )
    avatar: str | None = Field(
        default=None,
        description='Путь к файлу с аватаркой сотрудника',
    )
    avatar_big: str | None = Field(
        default=None,
        description='Путь к файлу с аватаркой сотрудника в большем разрешении',
    )
    rating: float | None = Field(
        default=None,
        description='Рейтинг сотрудника',
    )
    votes_count: int | None = Field(
        default=None,
        description='Количество голосов',
    )


class VisitClient(BaseModel):
    id: int = Field(
        default=...,
        description='Идентификатор клиента',
    )
    name: str = Field(
        default=...,
        description='Имя клиента',
    )
    surname: str | None = Field(
        default=None,
        description='Фамилия клиента',
    )
    patronymic: str | None = Field(
        default=None,
        description='Отчество клиента',
    )
    phone: str = Field(
        default=...,
        description='Номер телефона клиента',
    )
    card: str | None = Field(
        default=None,
        description='Номер карты клиента',
    )
    email: str | None = Field(
        default=None,
        description='Email клиента',
    )
    success_visits_count: int | None = Field(
        default=None,
        description='Количество успешных визитов',
    )
    fail_visits_count: int | None = Field(
        default=None,
        description='Количество отмененных визитов',
    )


class Record(BaseModel):
    id: int = Field(
        default=...,
        description='Идентификатор записи',
    )
    company_id: int = Field(
        default=...,
        description='Идентификатор компании',
    )
    staff_id: int = Field(
        default=...,
        description='Идентификатор сотрудника',
    )
    services: list[dict] = Field(
        default=...,
        description='Массив услуг',
    )
    goods_transactions: list[dict] = Field(
        default=...,
        description='Массив товарных транзакций',
    )
    staff: Staff = Field(
        default=...,
        description='Информация о сотруднике',
    )
    client: VisitClient = Field(
        default=...,
        description='Информация о клиенте',
    )
    datetime: dt = Field(
        default=...,
        description='Дата визита',
    )
    create_date: d = Field(
        default=...,
        description='Дата создания записи',
    )
    comment: str | None = Field(
        default=None,
        description='Комментарий к визиту',
    )
    online: bool | None = Field(
        default=None,
        description='Онлайн запись или нет',
    )
    visit_attendance: int = Field(
        default=...,
        description='Статус визита',
    )
    attendance: int = Field(
        default=...,
        description='Статус записи',
    )
    confirmed: int = Field(
        default=...,
        description='Подтверждена ли запись',
    )
    seance_length: int = Field(
        default=...,
        description='Длительность визита',
    )


class VisitResponseData(BaseResponseData):
    attendance: int = Field(
        default=...,
        description='Статус визита',
    )
    datetime: dt = Field(
        default=...,
        description='Дата визита',
    )
    comment: int | None = Field(
        default=None,
        description='Комментарий',
    )
    records: list[Record] = Field(
        default=...,
        description='Массив записей',
    )


# endregion


########################################################################################################################
# region Получить детали визита
class Expense(BaseModel):
    id: int = Field(
        default=...,
        description='Идентификатор статьи платежа',
    )
    title: str = Field(
        default=...,
        description='Название статьи платежа',
    )


class Account(BaseModel):
    id: int = Field(
        default=...,
        description='Идентификатор кассы',
    )
    title: str = Field(
        default=...,
        description='Название кассы',
    )


class TransactionClient(BaseModel):
    id: str = Field(
        default=...,
        description='Идентификатор клиента',
    )
    name: str = Field(
        default=...,
        description='Имя клиента',
    )
    phone: str = Field(
        default=...,
        description='Номер телефона клиента',
    )


class PaymentTransaction(BaseModel):
    id: int = Field(
        default=...,
        description='Идентификатор транзакции оплаты',
    )
    document_id: int = Field(
        default=...,
        description='Идентификатор документа',
    )
    date: d = Field(
        default=...,
        description='Дата транзакции',
    )
    type_id: int = Field(
        default=...,
        description='Тип транзакции',
    )
    expense_id: int = Field(
        default=...,
        description='Идентификатор статьи платежа',
    )
    account_id: int = Field(
        default=...,
        description='Идентификатор кассы',
    )
    amount: float = Field(
        default=...,
        description='Сумма оплаты',
    )
    client_id: int = Field(
        default=...,
        description='Идентификатор клиента',
    )
    comment: str | None = Field(
        default=None,
        description='Комментарий',
    )
    expense: Expense | None = Field(
        default=None,
        description='Статья платежа',
    )
    account: Account | None = Field(
        default=None,
        description='Касса',
    )
    client: TransactionClient | None = Field(
        default=None,
        description='Информация о клиенте',
    )


class LoyaltyTransaction(BaseModel):
    id: int = Field(
        default=...,
        description='Идентификатор транзакции',
    )
    status_id: int = Field(
        default=...,
        description='Идентификатор статуса транзакции',
    )
    amount: float = Field(
        default=...,
        description='Сумма оплаты лояльностью',
    )
    type_id: int = Field(
        default=...,
        description='Тип транзакции лояльности',
    )
    program_id: int = Field(
        default=...,
        description='Идентификатор программы лояльности',
    )
    card_id: int = Field(
        default=...,
        description='Идентификатор карты лояльности',
    )
    salon_group_id: int = Field(
        default=...,
        description='ID сети салонов',
    )
    is_discount: bool = Field(
        default=...,
        description='Это скидка',
    )
    is_loyalty_withdraw: bool = Field(
        default=...,
        description='Это снятие по программе лояльности',
    )


class KkmTransaction(BaseModel):
    id: int = Field(
        default=...,
        description='Идентификатор транзакции',
    )
    print_date: d = Field(
        default=...,
        description='Дата печати чека',
    )
    printed_count: int = Field(
        default=...,
        description='Количество печатей',
    )
    sum: float = Field(
        default=...,
        description='Сумма оплаты',
    )


class KkmTransactionDetails(BaseModel):
    last_operation_type: int = Field(
        default=...,
        description='Тип последней операции ККМ',
    )
    transactions: list[KkmTransaction] = Field(
        default=...,
        description='Транзакции ККМ',
    )


class Item(BaseModel):
    id: int = Field(
        default=...,
        description='Идентификатор сущности',
    )
    item_id: int = Field(
        default=...,
        description='Идентификатор товара или услуги',
    )
    item_type_id: int = Field(
        default=...,
        description='Тип сущности',
    )
    record_id: int = Field(
        default=...,
        description='Идентификатор записи',
    )
    item_title: str = Field(
        default=...,
        description='Название услуги или товара',
    )
    amount: float = Field(
        default=...,
        description='Количество',
    )
    cost: float = Field(
        default=...,
        description='Конечная стоимость',
    )


class VisitDetailsData(BaseModel):
    payment_transactions: list[PaymentTransaction] = Field(
        default=...,
        description='Транзакции оплаты',
    )
    loyalty_transactions: list[LoyaltyTransaction] = Field(
        default=...,
        description='Транзакции лояльности',
    )
    kkm_transaction_details_container: KkmTransactionDetails | None = Field(
        default=None, description='Детали ККМ транзакций'
    )
    items: list[Item] = Field(
        default=...,
        description='Товары или услуги',
    )


# endregion


########################################################################################################################
# region Изменить визит
class NewTransaction(BaseModel):
    id: int = Field(
        default=...,
        description='Идентификатор финансовой транзакции',
    )
    amount: float = Field(
        default=...,
        description='Сумма',
    )
    account_id: int = Field(
        default=...,
        description='Идентификатор кассы',
    )


class GoodsTransaction(BaseModel):
    id: int = Field(
        default=...,
        description='Идентификатор складской транзакции',
    )
    title: str = Field(
        default=...,
        description='Название товара',
    )
    barcode: str = Field(
        default=...,
        description='Штрихкод',
    )
    article: str = Field(
        default=...,
        description='Артикул',
    )
    amount: str = Field(
        default=...,
        description='Количество',
    )
    cost_per_unit: str = Field(
        default=...,
        description='Цена за единицу',
    )
    price: str = Field(
        default=...,
        description='Стоимость',
    )
    cost: str = Field(
        default=...,
        description='Цена продажи',
    )
    operation_unit_type: int = Field(
        default=...,
        description='Тип единицы измерения',
    )
    master_id: str = Field(
        default=...,
        description='Идентификатор сотрудника',
    )
    storage_id: str = Field(
        default=...,
        description='Идентификатор склада',
    )
    good_id: str = Field(
        default=...,
        description='Идентификатор товара',
    )
    discount: str = Field(
        default=...,
        description='Скидка',
    )


class Service(BaseModel):
    id: int = Field(
        default=...,
        description='Идентификатор услуги',
    )
    title: str = Field(
        default=...,
        description='Название услуги',
    )
    cost: float = Field(
        default=...,
        description='Итоговая стоимость услуги',
    )
    cost_per_unit: float = Field(
        default=...,
        description='Цена за единицу',
    )
    discount: float = Field(
        default=...,
        description='Скидка',
    )
    first_cost: float = Field(
        default=...,
        description='Начальная стоимость услуги',
    )
    record_id: int = Field(
        default=...,
        description='Идентификатор записи',
    )


# endregion


########################################################################################################################
# region Чек PDF по визиту
# TODO: Дописать

# endregion
