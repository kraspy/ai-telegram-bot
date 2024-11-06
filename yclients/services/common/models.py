from datetime import datetime as dt
from datetime import date as d
from pydantic import BaseModel, Field

from ..common.enums import CommentType


########################################################################################################################
# region Запрос
class BaseQueryParamsModel(BaseModel):
    '''Базовая модель для query-параметров, если будут общие параметры для всех запросов.'''

    pass


class BaseBodyModel(BaseModel):
    '''Базовая модель для тела запроса, чтобы можно было переопределить общие поля.'''

    pass


class BaseRequestModel(BaseModel):
    '''Базовая модель для запросов, содержащая query и body.'''

    query: BaseQueryParamsModel | None = Field(
        default=None,
        description='Query-параметры запроса',
    )
    body: BaseBodyModel | None = Field(
        default=None,
        description='Body запроса',
    )


# endregion


########################################################################################################################
# region Ответ
class BaseResponseModel(BaseModel):
    pass


class BaseResponseData(BaseModel):
    pass


class DefaultResponse(BaseResponseModel):
    '''
    Модель ответа API по умолчанию.

    Аргументы:
    - success: Статус успешности выполнения запроса.
    - data: Данные ответа.
    - meta: Пустые метаданные.
    '''

    success: bool = Field(default=..., description='Статус успешности выполнения запроса')
    data: BaseResponseData
    meta: list = Field(default=[], description='Метаданные (Пустые)')


class BaseMeta(BaseModel):
    pass


# endregion


########################################################################################################################
# region Ошибки Ответов


class BaseErrorModel(BaseModel):
    '''
    Базовая ошибка.
    '''

    success: bool = False
    data: None = None
    meta: dict


# endregion


# Клиент
class BaseClient(BaseModel):
    '''
    Базовая клиента.

    Содержит основную информацию о клиенте, включая личные данные, контактную информацию,
    предпочтения по SMS рассылкам, баланс и категориальные данные.

    Attributes:
        name (str): Имя клиента.
        surname (str): Фамилия клиента (необязательное).
        patronymic (str): Отчество клиента (необязательное).
        phone (str): Телефон клиента.
        email (str): Email клиента (необязательное).
        sex_id (int): Пол клиента (1 - мужской, 2 - женский, 0 - не известен).
        importance_id (int): Класс важности клиента (0 - нет, 1 - бронза, 2 - серебро, 3 - золото).
        discount (float): Скидка клиента.
        card (str): Номер карты клиента.
        birth_date (str): Дата рождения клиента в формате yyyy-mm-dd.
        comment (str): Комментарий о клиенте.
        spent (float): Сумма, которую клиент потратил на момент добавления.
        balance (float): Текущий баланс клиента.
        sms_check (int): Статус отправки SMS-поздравлений (1 - поздравлять, 0 - не поздравлять).
        sms_not (int): Исключить клиента из SMS рассылок (1 - исключить, 0 - не исключать).
        categories (list[int]): Список идентификаторов категорий клиента.
        custom_fields (dict): Дополнительные пользовательские поля клиента в формате "api-key": "value".
    '''

    name: str = Field(
        default=...,
        description='Имя клиента',
    )
    surname: str = Field(
        default=None,
        description='Фамилия клиента',
    )
    patronymic: str = Field(
        default=None,
        description='Отчество клиента',
    )
    phone: str = Field(
        default=...,
        description='Телефон клиента',
    )
    email: str = Field(
        default=None,
        description='Email клиента',
    )
    sex_id: int = Field(
        default=None,
        description='Пол клиента (1 - мужской, 2 - женский, 0 - не известен)',
    )
    importance_id: int = Field(
        default=None, description='Класс важности клиента (0 - нет, 1 - бронза, 2 - серебро, 3 - золото)'
    )
    discount: float = Field(
        default=None,
        description='Скидка клиента',
    )
    card: str = Field(
        default=None,
        description='Номер карты клиента',
    )
    birth_date: d = Field(
        default=None,
        description='Дата рождения клиента в формате yyyy-mm-dd',
    )
    comment: str = Field(
        default=None,
        description='Комментарий',
    )
    spent: float = Field(
        default=None,
        description='Сколько потратил средств в компании на момент добавления',
    )
    balance: float = Field(
        default=None,
        description='Баланс клиента',
    )
    sms_check: int = Field(
        default=None,
        description='1 - Поздравлять с Днем Рождения по SMS, 0 - не поздравлять',
    )
    sms_not: int = Field(
        default=None,
        description='1 - Исключить клиента из SMS рассылок, 0 - не исключать',
    )
    categories: list[int] = Field(
        default=None,
        description='Массив идентификаторов категорий клиента',
    )
    custom_fields: dict = Field(
        default=None,
        description='Массив дополнительных полей клиента в виде пар "api-key": "value"',
    )


# Запись
class BaseRecord(BaseModel):
    id: int = Field(
        default=...,
        description='ID записи',
    )
    comment: str = Field(
        default=None,
        description='Комментарий',
    )
    date: dt = Field(
        default=...,
        description='Дата записи в формате date-time',
    )
    visit_id: int = Field(
        default=...,
        description='ID визита',
    )
    attendance: int = Field(
        default=...,
        description='Статус посещения',
    )
    services: list = Field(  # TODO: Тут можно доработать (см. документацию YClients)
        default=...,
        description='Список услуг, объект модели "Услуга в записи истории посещений клиента"',
    )
    staff: dict = Field(  # TODO: Тут можно доработать (см. документацию YClients)
        default=...,
        description='Сотрудник, оказавший услугу, объект модели "Сотрудник с Должностью"',
    )
    company: dict = Field(  # TODO: Тут можно доработать (см. документацию YClients)
        default=...,
        description='Минимальная информация о филиале, объект модели "Филиал"',
    )
    tips: dict = Field(  # TODO: Тут можно доработать (см. документацию YClients)
        default=None,
        description='Данные о чаевых: объект модели "Наличие чаевых без суммы или "Суммарные чаевые"',
    )
    comer: dict | None = Field(  # TODO: Тут можно доработать (см. документацию YClients)
        default=None,
        description='Данные о посетителе, объект модели "Посетитель". Если не указан, поле не выводится.',
    )


# Файл комментария
class BaseCommentFile(BaseModel):
    link: str = Field(
        default=...,
        description='Ссылка на скачивание файла в карточке клиента.',
    )
    filename: str = Field(
        default=...,
        description='Название файла в карточке клиента.',
    )


# Пользователь комментария
class BaseCommentUser(BaseModel):
    id: int = Field(
        default=...,
        description='Идентификатор пользователя.',
    )
    name: str = Field(
        default=...,
        description='Имя пользователя.',
    )
    avatar: str = Field(
        default=None,
        description='Аватар пользователя.',
    )


# Комментарий к клиенту
class BaseClientComment(BaseModel):
    id: int = Field(
        default=...,
        description='Идентификатор комментария к клиенту.',
    )
    create_date: dt = Field(
        default=...,
        description='Дата и время создания комментария к клиенту.',
    )
    update_date: dt = Field(
        default=...,
        description='Дата и время последнего обновления комментария к клиенту.',
    )
    type: CommentType = Field(
        default=...,
        description='Тип комментария ("default" или "file").',
    )
    text: str = Field(
        default=None,
        description='Текст комментария (для "default").',
    )
    files: list[BaseCommentFile] = Field(
        default=list,
        description='Файлы, загруженные в карточку клиента (для "file").',
    )
    user: BaseCommentUser = Field(
        default=None,
        description='Пользователь, оставивший комментарий.',
    )


# Услуга
class BaseService(BaseModel):
    '''
    Базовая модель для услуги.

    Attributes:
        id (int): Уникальный идентификатор услуги.
        title (str): Название услуги.
        cost (float): Итоговая стоимость услуги.
        discount (float | None): Скидка на услугу.
    '''

    id: int = Field(..., description='Уникальный идентификатор услуги')
    title: str = Field(..., description='Название услуги')
    cost: float = Field(..., description='Итоговая стоимость услуги')
    discount: float | None = Field(None, description='Скидка на услугу')


# Товар
class BaseGoodsItem(BaseModel):
    id: int = Field(
        default=...,
        description='ID товара',
    )
    title: str = Field(
        default=...,
        description='Наименование товара',
    )
    amount: int = Field(
        default=...,
        description='Количество проданного товара',
    )
    unit: str = Field(
        default=...,
        description='Единица измерения проданного товара',
    )
    cost_per_unit: float = Field(
        default=...,
        description='Стоимость за единицу товара',
    )
    first_cost: float = Field(
        default=...,
        description='Общая стоимость товара без скидки',
    )
    discount_percent: float = Field(
        default=...,
        description='Процент скидки',
    )
    cost_to_pay: float = Field(
        default=...,
        description='Стоимость товара с учетом скидки',
    )
    paid_sum: float = Field(
        default=...,
        description='Оплаченная сумма',
    )
    payment_status: str = Field(
        default=...,
        description='Статус оплаты',
    )


# Транзакиця
class BaseTransaction(BaseModel):
    '''
    Базовая модель для транзакции.

    Attributes:
        id (int): Уникальный идентификатор транзакции.
        date (datetime): Дата транзакции.
        amount (float): Сумма транзакции.
        comment (str | None): Комментарий к транзакции.
    '''

    id: int = Field(
        default=...,
        description='ID транзакции по продаже товара',
    )
    comment: str = Field(
        default=None,
        description='Комментарий к продаже',
    )
    date: dt = Field(
        default=...,
        description='Дата продажи',
    )
    visit_id: int = Field(
        default=...,
        description='ID визита. Равно 0, если нет связи с визитом',
    )
    record_id: int = Field(
        default=...,
        description='ID записи. Равно 0, если нет связи с записью',
    )
    goods: list[BaseGoodsItem] = Field(
        default=...,
        description='Список проданных товаров',
    )
    staff: dict = Field(  # TODO: Тут можно доработать (см. документацию YClients)
        default=...,
        description='Сотрудник, продавший товар',
    )
    company: dict = Field(  # TODO: Тут можно доработать (см. документацию YClients)
        default=...,
        description='Минимальная информация о салоне, в котором был продан товар',
    )


# Сотрудник
class BaseStaff(BaseModel):
    '''
    Базовая модель для сотрудника.

    Attributes:
        id (int): Уникальный идентификатор сотрудника.
        name (str): Имя сотрудника.
        position (str | None): Должность сотрудника.
        rating (float | None): Рейтинг сотрудника (от 0 до 5).
    '''

    id: int = Field(..., description='Уникальный идентификатор сотрудника')
    name: str = Field(..., description='Имя сотрудника')
    position: str | None = Field(None, description='Должность сотрудника')
    rating: float | None = Field(None, description='Рейтинг сотрудника (от 0 до 5)')
