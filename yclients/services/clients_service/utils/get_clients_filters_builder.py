from typing import Any

from ..models.utils.get_clients_filter import (
    IDFilterState,
    SoldAmountState,
    QuickSearchState,
    ImportanceState,
    HasMobileAppState,
    CategoryState,
    HasPassteamCardState,
    PassteamCardState,
    BirthdayState,
    GenderState,
    RecordState,
    ClientState,
)

from ..models import GetClientsRequestBody, GetClientsRequest


class ClientsSearchRequestBuilder:
    def __init__(self):
        self.page = None
        self.page_size = None
        self.fields = []
        self.order_by = None
        self.order_by_direction = 'ASC'
        self.operation = 'AND'
        self.filters = []

    def set_page(self, page: int):
        '''Устанавливает номер страницы.'''
        self.page = page
        return self

    def set_page_size(self, page_size: int):
        '''Устанавливает количество записей на страницу.'''
        self.page_size = page_size
        return self

    def set_fields(self, fields: list[str]):
        '''Устанавливает поля для возврата.'''
        self.fields = fields
        return self

    def set_order_by(self, order_by: str, direction: str = 'ASC'):
        '''Устанавливает поле для сортировки и направление сортировки.'''
        self.order_by = order_by
        self.order_by_direction = direction
        return self

    def set_operation(self, operation: str):
        '''Устанавливает тип операции (AND/OR)'''
        self.operation = operation
        return self

    def add_id_filter(self, ids: list[int]):
        '''Добавляет фильтр по ID.'''
        id_filter = {
            'type': 'id',
            'state': IDFilterState(value=ids).model_dump(),
        }
        self.filters.append(id_filter)
        return self

    def add_sold_amount_filter(self, from_value: float, to_value: float):
        '''Добавляет фильтр по сумме продаж.'''
        sold_amount_filter = {
            'type': 'sold_amount',
            'state': SoldAmountState(
                from_value=from_value,
                to_value=to_value,
            ).model_dump(),
        }
        self.filters.append(sold_amount_filter)
        return self

    def add_quick_search_filter(self, search_term: str):
        '''Добавляет фильтр для быстрого поиска.'''
        quick_search_filter = {
            'type': 'quick_search',
            'state': QuickSearchState(value=search_term).model_dump(),
        }
        self.filters.append(quick_search_filter)
        return self

    def add_importance_filter(self, importance: list[int]):
        '''Добавляет фильтр по важности.'''
        importance_filter = {
            'type': 'importance',
            'state': ImportanceState(value=importance).model_dump(),
        }
        self.filters.append(importance_filter)
        return self

    def add_has_mobile_app_filter(self, has_mobile_app: bool):
        '''Добавляет фильтр по наличию мобильного приложения.'''
        has_mobile_app_filter = {
            'type': 'has_mobile_app',
            'state': HasMobileAppState(value=has_mobile_app).model_dump(),
        }
        self.filters.append(has_mobile_app_filter)
        return self

    def add_category_filter(self, category_ids: list[int]):
        '''Добавляет фильтр по категориям.'''
        category_filter = {
            'type': 'category',
            'state': CategoryState(value=category_ids).model_dump(),
        }
        self.filters.append(category_filter)
        return self

    def add_has_passteam_card_filter(self, has_passteam_card: bool):
        '''Добавляет фильтр по наличию Passteam-карты.'''
        has_passteam_card_filter = {
            'type': 'has_passteam_card',
            'state': HasPassteamCardState(value=has_passteam_card).model_dump(),
        }
        self.filters.append(has_passteam_card_filter)
        return self

    def add_passteam_card_ids_filter(self, passteam_card_ids: list[int]):
        '''Добавляет фильтр по ID Passteam-карты.'''
        passteam_card_ids_filter = {
            'type': 'passteam_card_ids',
            'state': PassteamCardState(value=passteam_card_ids).model_dump(),
        }
        self.filters.append(passteam_card_ids_filter)
        return self

    def add_birthday_filter(self, birthday_from: str, birthday_to: str):
        '''Добавляет фильтр по дате рождения.'''
        birthday_filter = {
            'type': 'birthday',
            'state': BirthdayState(
                from_value=birthday_from,
                to_value=birthday_to,
            ).model_dump(),
        }
        self.filters.append(birthday_filter)
        return self

    def add_gender_filter(self, gender: list[int]):
        '''Добавляет фильтр по полу.'''
        gender_filter = {
            'type': 'gender',
            'state': GenderState(value=gender).model_dump(),
        }
        self.filters.append(gender_filter)
        return self

    def add_record_filter(self, record: dict[str, Any]):
        '''Добавляет фильтр по записи.'''
        record_filter = {
            'type': 'record',
            'state': RecordState(value=record).model_dump(),
        }
        self.filters.append(record_filter)
        return self

    def add_client_filter(self, client_ids: dict[str, Any]):
        '''Добавляет фильтр по клиентам.'''
        client_filter = {
            'type': 'client',
            'state': ClientState(value=client_ids).model_dump(),
        }
        self.filters.append(client_filter)
        return self

    def build(self) -> GetClientsRequest:
        '''Генерирует итоговый запрос поиска клиентов.'''
        return GetClientsRequest(
            body=GetClientsRequestBody(
                page=self.page,
                page_size=self.page_size,
                fields=self.fields if self.fields else None,
                order_by=self.order_by,
                order_by_direction=self.order_by_direction,
                operation=self.operation,
                filters=self.filters if self.filters else None,
            ),
        )
