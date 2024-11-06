from typing import Any

from ..models.requests import BookRecordRequestBody, BookRecordRequest
from ..models._additional import Appointment


class BookRequestBuilder:
    def __init__(self, phone: str, fullname: str):
        self.phone = phone
        self.fullname = fullname
        self.email = ''  # QUESTION: YCLIENTS -> Почему email стал обязательным?
        self.code: int | None = None
        self.comment: str | None = None
        self.type: str | None = None
        self.notify_by_sms: int | None = None
        self.notify_by_email: int | None = None
        self.api_id: int | None = None
        self.custom_fields: dict[str, Any] | None = None
        self.appointments: list[Appointment] = []

    def set_email(self, email):
        self.email = email
        return self

    def set_code(self, code: int):
        self.code = code
        return self

    def set_comment(self, comment: str):
        self.comment = comment
        return self

    def set_type(self, type_: str):
        self.type = type_
        return self

    def set_notify_by_sms(self, notify_by_sms: int):
        self.notify_by_sms = notify_by_sms
        return self

    def set_notify_by_email(self, notify_by_email: int):
        self.notify_by_email = notify_by_email
        return self

    def set_api_id(self, api_id: int):
        self.api_id = api_id
        return self

    def set_custom_fields(self, custom_fields: dict[str, Any]):
        self.custom_fields = custom_fields
        return self

    def add_appointment(self, appointment: Appointment):
        self.appointments.append(appointment)
        return self

    def build(self) -> BookRecordRequest:
        return BookRecordRequest(
            body=BookRecordRequestBody(
                phone=self.phone,
                fullname=self.fullname,
                email=self.email,
                code=self.code,
                comment=self.comment,
                type=self.type,
                notify_by_sms=self.notify_by_sms,
                notify_by_email=self.notify_by_email,
                api_id=self.api_id,
                custom_fields=self.custom_fields,
                appointments=self.appointments,
            )
        )
