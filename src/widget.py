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
        tail = number[-4:]
        return f"{name} **{tail}"
    else:
        masked_number = get_mask_card_number(number)
        return f"{name} {masked_number}"


def get_date(date_str: str) -> str:
    """Функция принимает строку с датой и возвращает её в формате ДД.ММ.ГГГГ"""
    if not date_str or len(date_str) <10:
        return ""

    year = date_str[:4]
    month = date_str[5:7]
    day = date_str[8:10]

    return f"{day}.{month}.{year}"


# Этот блок для проверки
if __name__ == "__main__":
    test_card = "Visa Platinum 7000792289606361"
    test_account = "Счёт 73654108430135874305"
    test_iso_date = "2024-03-11Т02:26:18.671407"

    print(mask_account_card(test_card))
    print(mask_account_card(test_account))
    print("Результат форматирования даты:", get_date(test_iso_date))
