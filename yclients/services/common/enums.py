from enum import Enum


class HTTPMethod(str, Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    PATCH = 'PATCH'
    DELETE = 'DELETE'


class PaymentStatus(str, Enum):
    NOT_PAID = 'not_paid'  # Визит неоплачен, никаких оплат не было
    PAID_NOT_FULL = 'paid_not_full'  # Визит оплачен частично
    PAID_FULL = 'paid_full'  # Визит оплачен полностью, без переплаты
    PAID_OVER = 'paid_over'  # По визиту есть переплата


class CommentType(str, Enum):
    default = 'default'
    file = 'file'


class ShippingChannel(str, Enum):
    whatsapp = 'whatsapp'
    sms = 'sms'


class MessageStatusEnum(int, Enum):
    delivered = 1
    not_delivered = 2
