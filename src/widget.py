from datetime import datetime

from src.masks import get_mask_account_number, get_mask_card_number


def mask_account_card(info_string: str) -> str:
    """Маскирует номер карты или счёта, переданный в виде единой строки."""
    if not info_string or not info_string.strip():
        return ""

    parts = info_string.split()
    if len(parts) == 1:
        return info_string

    # Разделяем строку на цифры номера и текстовое название
    number = "".join([p for p in parts if p.isdigit()])
    name = " ".join([p for p in parts if not p.isdigit()])

    # Проверяем, счет это или карта, и вызываем нужную маску
    if "счет" in name.lower():
        return f"{name} {get_mask_account_number(number)}"
    else:
        return f"{name} {get_mask_card_number(number)}"


def get_date(date_str: str) -> str:
    """Функция принимает строку с датой и возвращает её в формате ДД.ММ.ГГГГ"""
    dt_obj = datetime.fromisoformat(date_str)
    return dt_obj.strftime("%d.%m.%Y")


if __name__ == "__main__":
    test_card = "Visa Platinum 700079228906361"
    test_account = "Счет 73654108430135874305"
    test_iso_date = "2024-03-11T02:26:18.671407"

    print(mask_account_card(test_card))
    print(mask_account_card(test_account))
    print(f"Результат форматирования даты: {get_date(test_iso_date)}")
