from datetime import datetime

from src.masks import get_mask_account_number, get_mask_card_number


def mask_account_card(info_string: str) -> str:
    """Маскирует номер карты или счёта, переданный в виде единой строки."""
    if not info_string or not info_string.strip():
        return ""

    parts = info_string.split()

    if len(parts) < 2:
        return info_string

    number = parts[-1]
    name = " ".join(parts[:-1])

    if "счет" in name.lower() or "счёт" in name.lower():
        masked_number = get_mask_account_number(number)
        return f"{name} {masked_number}"
    else:
        # Получаем номер из masks
        masked_number = get_mask_card_number(number)
        return f"{name} {masked_number}"


def get_date(date_str: str) -> str:
    """Функция принимает строку с датой и возвращает её в формате ДД.ММ.ГГГГ"""
    if not date_str:
        return ""

    # Разбираем ISO-строку с помощью встроенного модуля datetime
    dt_obj = datetime.fromisoformat(date_str)

    # Форматируем в строку вида ДД.ММ.ГГГГ
    return dt_obj.strftime("%d.%m.%Y")
