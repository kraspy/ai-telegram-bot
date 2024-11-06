from pydantic import Field
from datetime import datetime
from ...common.models import BaseRequestModel, BaseQueryParamsModel, BaseBodyModel

########################################################################################################################
# region Комментарии


class GetCommentsQueryParams(BaseQueryParamsModel):
    '''
    Модель для передачи query-параметров при получении комментариев.

    Аргументы:
    - start_date: Дата начала выборки комментариев в формате ISO8601.
    - end_date: Дата окончания выборки комментариев в формате ISO8601.
    - staff_id: ID сотрудника для фильтрации комментариев.
    - rating: Фильтр по оценке комментария.
    - page: Номер страницы результатов.
    - count: Количество комментариев на странице.
    '''

    start_date: datetime | None = Field(
        default=None,
        description='Дата начала в формате ISO8601',
    )
    end_date: datetime | None = Field(
        default=None,
        description='Дата окончания в формате ISO8601',
    )
    staff_id: int | None = Field(
        default=None,
        description='ID сотрудника',
    )
    rating: int | None = Field(
        default=None,
        description='Фильтр по оценке в рейтинге',
    )
    page: int | None = Field(
        default=None,
        description='Номер страницы',
    )
    count: int | None = Field(
        default=None,
        description='Количество комментариев на странице',
    )


class GetCommentsRequest(BaseRequestModel):
    '''
    Модель запроса для получения комментариев.

    Аргументы:
    - query: Query-параметры запроса.
    '''

    query: GetCommentsQueryParams = Field(
        default=...,
        description='Query-параметры запроса',
    )


class CreateCommentBody(BaseBodyModel):
    '''
    Модель тела запроса для создания нового комментария.

    Аргументы:
    - mark: Оценка от 1 до 5.
    - text: Текст комментария.
    - name: Имя пользователя для отображения на странице с отзывами.
    '''

    mark: int = Field(
        default=...,
        ge=1,
        le=5,
        description='Оценка от 1 до 5',
    )
    text: str = Field(
        default=...,
        description='Текст комментария',
    )
    name: str = Field(
        default=...,
        description='Имя пользователя для отображения на странице с отзывами',
    )


class CreateCommentRequest(BaseRequestModel):
    '''
    Модель запроса для создания нового комментария.

    Аргументы:
    - body: Тело запроса с информацией о комментарии.
    '''

    body: CreateCommentBody = Field(
        default=...,
        description='Body запроса',
    )


# endregion
