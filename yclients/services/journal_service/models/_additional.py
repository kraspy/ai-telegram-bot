from pydantic import BaseModel, Field


class JournalSeance(BaseModel):
    time: str = Field(
        default=...,
        description='Время сеанса',
    )
    is_free: bool = Field(
        default=...,
        description='Свободно время или нет',
    )
