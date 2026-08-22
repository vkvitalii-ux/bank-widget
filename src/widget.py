from src.masks import get_mask_card_number


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
        tail = number[-4:]
        return f"{name} **{tail}"
    else:
        masked_number = get_mask_card_number(number)
        return f"{name} {masked_number}"


def get_date(date_str: str) -> str:
    """Функция принимает строку с датой и возвращает её в формате ДД.ММ.ГГГГ"""
    if not date_str or len(date_str) < 10:
        return ""

    year = date_str[:4]
    month = date_str[5:7]
    day = date_str[8:10]

    return f"{day}.{month}.{year}"



