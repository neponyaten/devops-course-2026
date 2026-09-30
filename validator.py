import re


def validate_email(email: str) -> bool:
    """Базовая валидация email."""
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return bool(re.match(pattern, email))


def validate_phone(phone: str) -> bool:
    """Валидация российского номера."""
    cleaned = phone.replace('-', '').replace(' ', '')
    return bool(re.match(r'^\+?7\d{10}$', cleaned))


def validate_snils(snils: str) -> bool:
    """Валидация СНИЛС."""
    digits = ''.join(ch for ch in snils if ch.isdigit())
    return len(digits) == 11 and digits[:3] != '000'
