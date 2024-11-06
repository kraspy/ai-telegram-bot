from datetime import datetime as dt
from pydantic import BaseModel, Field


class Position(BaseModel):
    id: int = Field(
        default=...,
        description='ID должности',
    )
    title: str = Field(
        default=...,
        description='Название должности',
    )


class Staff(BaseModel):
    id: int = Field(
        default=...,
        description='ID сотрудника',
    )
    name: str = Field(
        default=...,
        description='Имя сотрудника',
    )
    specialization: str = Field(
        default=...,
        description='Специализация сотрудника',
    )
    position: Position = Field(
        default=...,
        description='Должность сотрудника',
    )
    show_rating: bool = Field(
        default=...,
        description='Показывать ли рейтинг сотрудника',
    )
    rating: float = Field(
        default=...,
        description='Рейтинг сотрудника (от 0 до 5)',
    )
    votes_count: int = Field(
        default=...,
        description='Количество голосов, поставивших сотруднику оценку',
    )
    avatar: str = Field(
        default=...,
        description='Путь к аватарке сотрудника',
    )
    comments_count: int = Field(
        default=...,
        description='Количество комментариев сотруднику',
    )


class Company(BaseModel):
    id: int = Field(
        default=...,
        description='Идентификатор компании',
    )
    title: str = Field(
        default=...,
        description='Название компании',
    )
    country_id: int = Field(
        default=...,
        description='Идентификатор страны',
    )
    country: str = Field(
        default=...,
        description='Название страны компании',
    )
    city_id: int = Field(
        default=...,
        description='Идентификатор города',
    )
    city: str = Field(
        default=...,
        description='Название города компании',
    )
    phone: str = Field(
        default=...,
        description='Основной номер телефона компании',
    )
    phones: list[str] = Field(
        default=...,
        description='Все номера телефонов компании',
    )
    timezone: str = Field(
        default=...,
        description='Временная зона компании',
    )
    address: str = Field(
        default=...,
        description='Адрес компании',
    )
    coordinate_lat: float = Field(
        default=...,
        description='Широта компании',
    )
    coordinate_lon: float = Field(
        default=...,
        description='Долгота компании',
    )
    allow_delete_record: bool = Field(
        default=...,
        description='Можно ли удалять запись',
    )
    allow_change_record: bool = Field(
        default=...,
        description='Можно ли переносить запись',
    )
    site: str | None = Field(
        default=None,
        description='Сайт компании',
    )
    currency_short_title: str = Field(
        default=...,
        description='Символ валюты',
    )
    allow_change_record_delay_step: int = Field(
        default=...,
        description='Время до переноса записи',
    )
    allow_delete_record_delay_step: int = Field(
        default=...,
        description='Время до удаления записи',
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
        description='Стоимость услуги',
    )
    price_min: float = Field(
        default=...,
        description='Минимальная цена услуги',
    )
    price_max: float = Field(
        default=...,
        description='Максимальная цена услуги',
    )
    discount: float = Field(
        default=...,
        description='Скидка',
    )
    amount: int = Field(
        default=...,
        description='Количество заказанных услуг',
    )
    seance_length: int | None = Field(
        default=None, description='Длительность оказания услуги в секундах (только если задан фильтр по сотруднику)'
    )


class Record(BaseModel):
    id: int = Field(
        default=...,
        description='ID записи',
    )
    services: list[Service] = Field(
        default=...,
        description='Список услуг',
    )
    company: Company = Field(
        default=...,
        description='Параметры компании',
    )
    staff: Staff = Field(
        default=...,
        description='Параметры сотрудника',
    )
    clients_count: int = Field(
        default=...,
        description='Количество клиентов',
    )
    date: dt = Field(
        default=...,
        description='Дата сеанса',
    )
    datetime: dt = Field(
        default=...,
        description='Дата сеанса в формате ISO8601',
    )
    create_date: dt = Field(
        default=...,
        description='Дата создания записи',
    )
    comment: str = Field(
        default=...,
        description='Комментарий к записи',
    )
    deleted: bool = Field(
        default=...,
        description='Удалена ли запись',
    )
    attendance: int = Field(
        default=...,
        description='Статус посещения',
    )
    length: int = Field(
        default=...,
        description='Длительность сеанса',
    )
    notify_by_sms: int = Field(
        default=...,
        description='За сколько часов отправить SMS напоминание',
    )
    notify_by_email: int = Field(
        default=...,
        description='За сколько часов отправить Email напоминание',
    )
    master_requested: bool = Field(
        default=...,
        description='Был ли указан определенный специалист при записи (False если был указан "не имеет значения")',
    )
    online: bool = Field(
        default=...,
        description='Онлайн-запись или нет',
    )
    api_id: str | None = Field(
        default=None,
        description='Внешний идентификатор записи',
    )
    last_change_date: dt | None = Field(
        default=None,
        description='Дата последнего редактирования записи',
    )
    prepaid: bool | None = Field(
        default=None,
        description='Доступна ли онлайн-оплата для записи',
    )
    prepaid_confirmed: bool | None = Field(
        default=None,
        description='Статус онлайн-оплаты',
    )
    activity_id: int | None = Field(
        default=None,
        description='ID групповой записи',
    )
