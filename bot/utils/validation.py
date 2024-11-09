import re


def validate_fullname(fullname: str) -> bool:
    fullname = fullname.strip()

    parts = fullname.split()

    if len(parts) != 2:
        return False

    pattern = re.compile(r'^[А-ЯЁ][а-яё\-]*[а-яё]$')
    for part in parts:
        if not pattern.match(part):
            return False
    return True


def validate_phone(phone: str) -> str | None:
    digits = re.sub(r'\D', '', phone)

    if digits.startswith('8'):
        digits = digits[1:]
    elif digits.startswith('7'):
        digits = digits[1:]

    if len(digits) == 10 and digits.startswith('9'):
        formatted_number = f'7{digits}'
        return formatted_number
    else:
        return None
