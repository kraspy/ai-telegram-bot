from datetime import datetime as dt
from datetime import date as d
from pydantic import BaseModel, Field


# region Общие модели
class Staff(BaseModel):
    id: int = Field(
        default=...,
        description='Идентификатор сотрудника',
    )
    name: str = Field(
        default=...,
        description='Имя сотрудника',
    )
    company_id: int = Field(
        default=...,
        description='Идентификатор компании',
    )
    specialization: str | None = Field(
        default=None,
        description='Специализация',
    )
    position: list[str] | None = Field(
        default=None,
        description='Должности сотрудника',
    )
    rating: int | None = Field(
        default=None,
        description='Рейтинг',
    )
    show_rating: bool = Field(
        default=...,
        description='Отображать ли рейтинг',
    )
    comments_count: int | None = Field(
        default=None,
        description='Количество комментариев',
    )
    votes_count: int | None = Field(
        default=None,
        description='Количество голосов',
    )
    average_score: int | None = Field(
        default=None,
        description='Средний балл',
    )
    avatar: str | None = Field(
        default=None,
        description='Ссылка на аватар сотрудника',
    )
    prepaid: str | None = Field(
        default=None,
        description='Статус предоплаты',
    )


class Client(BaseModel):
    id: int = Field(
        default=...,
        description='Идентификатор клиента',
    )
    name: str | None = Field(
        default=None,
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
    phone: str | None = Field(
        default=None,
        description='Телефон клиента',
    )
    phone_code: str | None = Field(
        default=None,
        description='Код телефона клиента',
    )
    email: str | None = Field(
        default=None,
        description='Email клиента',
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
    manual_cost: float | None = Field(
        default=None,
        description='Стоимость, указанная вручную',
    )
    cost_per_unit: float | None = Field(
        default=None,
        description='Стоимость за единицу',
    )
    discount: float | None = Field(
        default=None,
        description='Скидка',
    )
    first_cost: float | None = Field(
        default=None,
        description='Начальная стоимость услуги (без учета скидок)',
    )
    amount: int | None = Field(
        default=None,
        description='Количество',
    )


class Record(BaseModel):
    id: int = Field(
        default=...,
        description='ID записи',
    )
    company_id: int = Field(
        default=...,
        description='ID компании',
    )
    staff: Staff = Field(
        default=...,
        description='Информация о сотруднике',
    )
    client: Client | None = Field(
        default=None,
        description='Информация о клиенте',
    )
    services: list[Service] = Field(
        default=...,
        description='Список услуг в записи',
    )
    date: d = Field(
        default=...,
        description='Дата записи в формате ISO',
    )
    comment: str | None = Field(
        default=None,
        description='Комментарий к записи',
    )


class StaffPosition(BaseModel):
    id: int = Field(
        default=...,
        description='Идентификатор должности',
    )
    title: str = Field(
        default=...,
        description='Название должности',
    )


# endregion


########################################################################################################################
# region  Создать новую запись
class ServiceCreate(BaseModel):
    id: int = Field(
        default=...,
        description='Идентификатор услуги',
    )
    first_cost: float = Field(
        default=...,
        description='Начальная стоимость услуги',
    )
    discount: float | None = Field(
        default=None,
        description='Скидка на услугу',
    )
    cost: float = Field(
        default=...,
        description='Итоговая стоимость услуги',
    )


class ClientCreate(BaseModel):
    phone: str = Field(
        default=...,
        description='Номер телефона клиента',
    )
    name: str | None = Field(
        default=None,
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
    email: str | None = Field(
        default=None,
        description='Эл. почта клиента',
    )


# endregion


########################################################################################################################
# region  Получить список записей партнёра
class Company(BaseModel):
    id: int = Field(
        default=...,
        description='Идентификатор компании',
    )
    title: str | None = Field(
        default=None,
        description='Название компании',
    )
    public_title: str | None = Field(
        default=None,
        description='Публичное название компании',
    )
    business_group_id: int | None = Field(
        default=None,
        description='Идентификатор группы бизнеса',
    )
    business_type_id: int | None = Field(
        default=None,
        description='Идентификатор типа бизнеса',
    )
    country_id: int | None = Field(
        default=None,
        description='Идентификатор страны',
    )
    city_id: int | None = Field(
        default=None,
        description='Идентификатор города',
    )
    timezone: str | None = Field(
        default=None,
        description='Часовой пояс',
    )
    timezone_name: str | None = Field(
        default=None,
        description='Название часового пояса',
    )
    coordinate_lat: float | None = Field(
        default=None,
        description='Широта',
    )
    coordinate_lon: float | None = Field(
        default=None,
        description='Долгота',
    )
    logo: str | None = Field(
        default=None,
        description='Логотип компании',
    )
    zip: int | None = Field(
        default=None,
        description='Почтовый индекс',
    )
    phone: str | None = Field(
        default=None,
        description='Телефон компании',
    )
    phones: list[str] | None = Field(
        default=None,
        description='Телефоны компании',
    )
    site: str | None = Field(
        default=None,
        description='Сайт компании',
    )
    allow_delete_record: bool = Field(
        default=...,
        description='Разрешено ли удалять записи',
    )
    allow_change_record: bool = Field(
        default=...,
        description='Разрешено ли изменять записи',
    )
    country: str | None = Field(
        default=None,
        description='Страна',
    )
    city: str | None = Field(
        default=None,
        description='Город',
    )


class RecordPartner(BaseModel):
    id: int = Field(
        default=...,
        description='Идентификатор записи',
    )
    date: d = Field(
        default=...,
        description='Дата записи',
    )
    datetime: dt = Field(
        default=...,
        description='Дата и время записи',
    )
    create_date: d = Field(
        default=...,
        description='Дата создания записи',
    )
    comment: str | None = Field(
        default=None,
        description='Комментарий к записи',
    )
    deleted: bool = Field(
        default=...,
        description='Флаг удаления записи',
    )
    attendance: int = Field(
        default=...,
        description='Статус посещаемости',
    )
    length: int = Field(
        default=...,
        description='Длительность услуги в секундах',
    )
    notify_by_sms: int | None = Field(
        default=None,
        description='Уведомление по SMS',
    )
    notify_by_email: int | None = Field(
        default=None,
        description='Уведомление по Email',
    )
    master_requested: bool = Field(
        default=...,
        description='Запрос мастера',
    )
    online: bool = Field(
        default=...,
        description='Запись онлайн',
    )
    api_id: str | None = Field(
        default=None,
        description='Идентификатор API',
    )
    last_change_date: d = Field(
        default=...,
        description='Дата последнего изменения',
    )
    prepaid: int | None = Field(
        default=None,
        description='Предоплата',
    )
    prepaid_confirmed: int | None = Field(
        default=None,
        description='Подтвержденная предоплата',
    )
    activity_id: int | None = Field(
        default=None,
        description='Идентификатор активности',
    )
    services: list[Service] = Field(
        default=...,
        description='Список услуг',
    )
    company: Company = Field(
        default=...,
        description='Информация о компании',
    )
    staff: Staff = Field(
        default=...,
        description='Информация о сотруднике',
    )
    client: Client = Field(
        default=...,
        description='Информация о клиенте',
    )


# endregion


########################################################################################################################
# Получить запись
class GetRecordData(BaseModel):
    id: int = Field(
        default=...,
        description='ID записи',
    )
    company_id: int = Field(
        default=...,
        description='Идентификатор компании',
    )
    staff_id: int = Field(
        default=...,
        description='Идентификатор сотрудника',
    )
    services: list[Service] = Field(
        default=...,
        description='Массив объектов с услугами в записи',
    )
    staff: Staff = Field(
        default=...,
        description='Информация о сотруднике',
    )
    client: Client | None = Field(
        default=None,
        description='Информация о клиенте',
    )
    date: d = Field(
        default=...,
        description='Дата сеанса',
    )
    datetime: dt = Field(
        default=...,
        description='Дата сеанса в ISO',
    )
    create_date: d = Field(
        default=...,
        description='Дата создания сеанса',
    )
    comment: str | None = Field(
        default=None,
        description='Комментарий к записи',
    )
    confirmed: int = Field(
        default=...,
        description='Статус подтверждения записи, 0 - не подтверждена, 1 - подтверждена',
    )
    seance_length: int = Field(
        default=...,
        description='Длительность сеанса',
    )
    attendance: int = Field(
        default=...,
        description='Статус записи (1 - пользователь пришел, -1 - не пришел)',
    )
    last_change_date: d = Field(
        default=...,
        description='Дата последнего изменения записи',
    )


# endregion


########################################################################################################################
# region  Изменить запись
class ServiceUpdate(BaseModel):
    id: int = Field(
        default=...,
        description='Идентификатор услуги',
    )
    first_cost: float | None = Field(
        default=None,
        description='Начальная стоимость услуги',
    )
    discount: float | None = Field(
        default=None,
        description='Скидка на услугу',
    )
    cost: float = Field(
        default=...,
        description='Итоговая стоимость услуги',
    )


class ClientUpdate(BaseModel):
    phone: str | None = Field(
        default=None,
        description='Номер телефона клиента',
    )
    name: str | None = Field(
        default=None,
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
    email: str | None = Field(
        default=None,
        description='Email клиента',
    )


# endregion

########################################################################################################################
# region  Удалить запись
# TODO: Дописать
# endregion
