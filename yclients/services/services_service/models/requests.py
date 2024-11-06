from pydantic import Field
from ...common.models import BaseRequestModel, BaseQueryParamsModel

########################################################################################################################
# region Получить список услуг / конкретную услугу


class ServicesQueryParams(BaseQueryParamsModel):
    '''
    Модель query-параметров для получения списка услуг или конкретной услуги.

    Аргументы:
    - staff_id: Идентификатор сотрудника (опционально).
    - category_id: Идентификатор категории услуг (опционально).
    '''

    staff_id: int | None = None
    category_id: int | None = None


class ServicesRequest(BaseRequestModel):
    '''
    Модель запроса для получения списка услуг или конкретной услуги.

    Аргументы:
    - query: Query-параметры для фильтрации услуг.
    '''

    query: ServicesQueryParams = Field(
        default=...,
        description='Query параметры для получения списка услуг или конкретной услуги',
    )


# endregion
