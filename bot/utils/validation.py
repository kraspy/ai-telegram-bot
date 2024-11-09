import re


def validate_fullname(fullname):
    '''Проверяет корректность полного имени.

    Args:
        fullname (str): Полное имя.

    Returns:
        bool: True, если имя корректно, иначе False.
    '''
    fullname = fullname.strip()
    parts = fullname.split()

    if len(parts) != 2:
        return False

    pattern = re.compile(r'^[А-ЯЁ][а-яё\-]*[а-яё]$')
    return all(pattern.match(part) for part in parts)


def validate_phone(phone):
    '''Проверяет и форматирует номер телефона.

    Args:
        phone (str): Номер телефона.

    Returns:
        str or None: Форматированный номер, если корректен, иначе None.
    '''
    digits = re.sub(r'\D', '', phone)

    if digits.startswith(('7', '8')):
        digits = digits[1:]

    if len(digits) == 10 and digits.startswith('9'):
        return f'7{digits}'
    else:
        return None
