from typing import Any
from pydantic import BaseModel, Field


# region Фильтры
class FilterState(BaseModel):
    pass


class IDFilterState(FilterState):
    value: list[int] = Field(
        default=...,
        description='Список ID клиентов для фильтрации',
    )


class IDFilter(BaseModel):
    type: str = Field(
        'id',
        description='Тип фильтра - ID',
    )
    state: IDFilterState = Field(
        default=...,
        description='Список ID для фильтрации',
    )


class SoldAmountState(BaseModel):
    from_value: float = Field(...)
    to_value: float = Field(...)


class SoldAmountFilter(BaseModel):
    type: str = Field(
        'sold_amount',
        description='Тип фильтра - Сумма продаж',
    )
    state: SoldAmountState = Field(
        default=None,
        description='Диапазон суммы продаж',
        json_schema_extra={
            'example': {'from': 0.0, 'to': 100.0},
        },
    )


class QuickSearchState(BaseModel):
    value: str


class QuickSearchFilter(BaseModel):
    type: str = Field(
        'quick_search',
        description='Тип фильтра - Быстрый поиск',
    )
    state: str = Field(
        default=None,
        description='Строка для быстрого поиска',
    )


class ImportanceState(BaseModel):
    value: list[int]


class ImportanceFilter(BaseModel):
    type: str = Field(
        'importance',
        description='Тип фильтра - Значимость',
    )
    state: list[int] = Field(
        default=None,
        description='Список значений важности',
    )


class HasMobileAppState(BaseModel):
    value: bool


class HasMobileAppFilter(BaseModel):
    type: str = Field(
        'has_mobile_app',
        description='Тип фильтра - Наличие мобильного приложения',
    )
    state: bool = Field(
        default=None,
        description='Булево значение, указывающее наличие мобильного приложения',
    )


class CategoryState(BaseModel):
    value: list[int]


class CategoryFilter(BaseModel):
    type: str = Field(
        'category',
        description='Тип фильтра - Категория',
    )
    state: list[int] = Field(
        default=None,
        description='Список идентификаторов категорий для фильтрации',
    )


class HasPassteamCardState(BaseModel):
    value: bool


class HasPassteamCardFilter(BaseModel):
    type: str = Field(
        'has_passteam_card',
        description='Тип фильтра - Наличие карты в системе Passteam',
    )
    state: bool = Field(
        default=None,
        description='Булево значение, указывающее наличие карты Passteam',
    )


class PassteamCardState(BaseModel):
    value: list[int]


class PassteamCardIDsFilter(BaseModel):
    type: str = Field(
        'passteam_card_ids',
        description='Тип фильтра - Идентификаторы карт Passteam',
    )
    state: list[str] = Field(
        default=None,
        description='Список идентификаторов карт в системе Passteam',
    )


class BirthdayState(BaseModel):
    from_value: str = Field(...)
    to_value: str = Field(...)


class BirthdayFilter(BaseModel):
    type: str = Field(
        'birthday',
        description='Тип фильтра - Дата рождения',
    )
    state: dict = Field(
        default=None,
        description='Диапазон даты рождения',
        json_schema_extra={'example': {'from': '2000-01-01', 'to': '2000-01-31'}},
    )


class GenderState(BaseModel):
    value: list[int]


class GenderFilter(BaseModel):
    type: str = Field(
        'gender',
        description='Тип фильтра - Пол',
    )
    state: list[int] = Field(
        default=None,
        description='Список значений пола',
    )


class RecordState(BaseModel):
    value: dict[str, Any]


class RecordFilter(BaseModel):
    type: str = Field(
        'record',
        description='Тип фильтра - Записи',
    )
    state: dict = Field(
        default=None,
        description='Фильтр по записям',
        json_schema_extra={
            'example': {
                'staff': {'value': [1, 2]},
                'service': {'value': [2, 3]},
                'service_category': {'value': [4, 5]},
                'status': {'value': [1]},
                'created': {'from': '2020-01-01', 'to': '2020-05-01'},
                'records_count': {'from': 1, 'to': 99999},
                'sold_amount': {'from': 1.001, 'to': 99999.09},
            }
        },
    )


class ClientState(BaseModel):
    value: dict[str, Any]


class ClientFilter(BaseModel):
    type: str = Field(
        'client',
        description='Тип фильтра - Клиенты',
    )
    state: dict = Field(
        default=None,
        description='Фильтр по клиентам',
        json_schema_extra={
            'example': {
                'id': {'value': [1, 2, 3]},
                'birthday': {'from': '2000-01-01', 'to': '2000-03-01'},
            }
        },
    )


# endregion
