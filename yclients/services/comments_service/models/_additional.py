from datetime import datetime as dt
from pydantic import BaseModel, Field


class RequestMeta(BaseModel):
    success: bool = Field(
        default=...,
        description='Статус успешности выполнения запроса',
    )
    meta: list[dict] | None = Field(
        default=list,
        description='Метаданные запроса',
    )


class Comment(BaseModel):
    id: int = Field(
        default=...,
        description='Идентификатор комментария',
    )
    type: int = Field(
        default=...,
        description='1 - комментарий к мастеру, 0 - к салону',
    )
    master_id: int | None = Field(
        default=None,
        description='ID мастера, если type = 1',
    )
    text: str = Field(
        default=...,
        description='Текст комментария',
    )
    date: dt = Field(
        default=...,
        description='Дата комментария в формате ISO8601',
    )
    rating: int = Field(
        default=...,
        description='Оценка от 1 до 5',
    )
    user_id: int = Field(
        default=...,
        description='ID пользователя, оставившего комментарий',
    )
    user_name: str = Field(
        default=...,
        description='Имя пользователя, оставившего комментарий',
    )
    user_avatar: str = Field(
        default=...,
        description='Аватар пользователя',
    )
    record_id: int | None = Field(
        default=None,
        description='ID записи, после которой был оставлен комментарий',
    )
