from datetime import date as d

MONTHS = {
    1: 'Января',
    2: 'Февраля',
    3: 'Марта',
    4: 'Апреля',
    5: 'Мая',
    6: 'Июня',
    7: 'Июля',
    8: 'Августа',
    9: 'Сентября',
    10: 'Октября',
    11: 'Ноября',
    12: 'Декабря',
}


def format_date(date: d) -> str:
    return f'{date.day} {MONTHS[date.month]}, {date.year}'


def format_service_title(service_title: str) -> str:
    SERVICE_EMOJI = {
        'Консультация косметолога': '🧖',
        'Чистка лица': '🧖',
        'Пилинги': '🧴',
        'Уход за кожей лица': '💧',
        'Массаж лица': '💆‍♀️',
        'Контурная пластика губ': '💋',
        'Ботулинотерапия': '💉',
        'Биоревитализация': '💧',
        'Коктейль Монако': '🍸',
        'Мезотерапия': '💉',
        'Восстановление волос и кожи головы': '💇‍♀️',
        'Коллагенотерапия': '💉',
    }
    emoji = SERVICE_EMOJI.get(service_title, '💆‍♀️')

    return f'{emoji} {service_title}'