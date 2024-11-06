from datetime import datetime as dt
from datetime import date as d
from pydantic import BaseModel, Field


class Appointment(BaseModel):
    id: int
    services: list[int]
    staff_id: int
    datetime: dt  # В формате ISO8601
    custom_fields: dict[str, str] | None = None


class AppointmentError(BaseModel):
    code: int
    message: str


########################################################################################################################
# region Список доступных услуг
class Service(BaseModel):
    id: int = Field(
        default=...,
        description='Идентификатор услуги',
    )
    title: str = Field(
        default=...,
        description='Название услуги',
    )
    category_id: int = Field(
        default=...,
        description='Идентификатор категории, которой принадлежит услуга',
    )
    weight: float = Field(
        default=...,
        description='Вес категории. При выводе услуги сортируются по весу, сначала более тяжелые',
    )
    price_min: float = Field(
        default=...,
        description='Минимальная стоимость услуги',
    )
    price_max: float = Field(
        default=...,
        description='Максимальная стоимость услуги',
    )
    discount: float = Field(
        default=...,
        description='Скидка по услуге',
    )
    comment: str = Field(
        default=...,
        description='Комментарий к услуге',
    )
    active: int = Field(
        default=...,
        description='Активная ли услуга',
    )
    prepaid: str = Field(
        default=...,
        description='Статус онлайн-оплаты',
    )
    sex: int = Field(
        default=...,
        description='Пол, для которого оказывается услуга',
    )
    seance_length: int | None = Field(
        default=None,
        description='Длительность оказания услуги в секундах (только если задан фильтр по сотруднику)',
    )
    image: str = Field(
        default=...,
        description='Изображение услуги',
    )


class Category(
    BaseModel,
):
    id: int = Field(
        default=...,
        description='Идентификатор категории',
    )
    title: str = Field(
        default=...,
        description='Название категории',
    )
    sex: int = Field(
        default=...,
        description='Принадлежность категории к полу (1 - мужской, 2 - женский, 0 - не задано,)',
    )
    weight: int = Field(
        default=...,
        description='Вес категории. При выводе категории сортируются по весу, сначала более тяжелые',
    )
    api_id: int = Field(
        default=...,
        description='Внешний идентификатор категории',
    )


class BookServicesResponseData(
    BaseModel,
):
    services: list[Service] = Field(
        default=...,
        description='Услуги, доступные для бронирования, с указанием категории',
    )
    category: list[Category] = Field(
        default=...,
        description='Массив категорий услуг',
    )


# endregion


########################################################################################################################
# region Список доступных дат
class BookableDatesData(BaseModel):
    booking_days: dict[str, list[int]] = Field(
        default=...,
        description='Массив дней, которые доступны для бронирования на указанные услуги',
    )
    booking_dates: list[d] = Field(
        default=...,
        description='Массив дат, когда есть свободные сеансы на услугу к выбранному сотруднику/организации',
    )
    working_days: dict[str, list[int]] = Field(
        default=...,
        description='Рабочие дни сотрудника/организации',
    )
    working_dates: list[d] = Field(
        default=...,
        description='Массив дат, когда работает сотрудник/организация',
    )


########################################################################################################################
# region Список доступных сеансов
class Seance(BaseModel):
    time: str = Field(
        default=...,
        description='Время сеанса (например, "17:30")',
    )
    seance_length: int = Field(
        default=...,
        description='Длительность сеанса в секундах',
    )
    datetime: dt = Field(
        default=...,
        description='Дата и время сеанса в формате ISO8601',
    )


# endregion


########################################################################################################################
# region Создать запись на сеанс
class BookRecordData(BaseModel):
    id: int
    record_id: int
    record_hash: str


# endregion


########################################################################################################################
# Перенести запись на сеанс


class CompanyModel(BaseModel):
    id: int
    title: str
    country_id: int
    country: str
    city_id: int
    city: str
    phone: str
    timezone: str
    address: str
    coordinate_lat: float
    coordinate_lon: float


class StaffModel(BaseModel):
    id: int
    name: str
    spec: str
    show_rating: bool
    rating: float
    votes_count: int
    avatar: str
    comments_count: int


class RescheduleRecordData(BaseModel):
    id: int
    services: list[Service]
    company: CompanyModel
    staff: StaffModel
    date: d
    create_date: d
    comment: str | None = None
    deleted: bool
    length: int
    notify_by_sms: int | None = 0
    notify_by_email: int | None = 0
    master_requested: bool
    online: bool
    api_id: str | None = None
