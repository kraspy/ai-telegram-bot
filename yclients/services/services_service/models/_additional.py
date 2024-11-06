from pydantic import BaseModel


class StaffModel(BaseModel):
    id: int
    seance_length: int


class ImageGroupModel(BaseModel):
    id: int
    entity: str
    entity_id: int
    images: dict


class ServiceModel(BaseModel):
    id: int
    title: str
    category_id: int | None
    price_min: float
    price_max: float
    discount: float | None
    comment: str | None
    weight: int | None
    active: int | None
    api_id: str | None
    staff: list[StaffModel] = []
    image_group: ImageGroupModel | None
