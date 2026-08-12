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

    if "счёт" in name.lower() or "счёт" in name.lower():
        masked_number = get_mask_account_number(number)
        return f"{name} {masked_number}"
    else:
        # Получаем номер из masks
        raw_masked_card = get_mask_card_number(number)

        # Вырезаем строго по индексам
        first_chunk = raw_masked_card[:4]
        second_chunk = raw_masked_card[4:8]
        third_chunk = raw_masked_card[8:12]
        last_chunk = raw_masked_card[-4:]

        card_format = f"{first_chunk} {second_chunk} {third_chunk} {last_chunk}"
        return f"{name} {card_format}"


def get_date(date_str: str) -> str:
    """Функция принимает строку с датой и возвращает её в формате ДД.ММ.ГГГГ"""
    if not date_str:
        return ""

    # Разбираем ISO-строку с помощью встроенного модуля datetime
    dt_obj = datetime.fromisoformat(date_str)

    # Форматируем в строку вида ДД.ММ.ГГГГ
    return dt_obj.strftime("%d.%m.%Y")


# Этот блок для проверки
if __name__ == "__main__":
    test_card = "Visa Platinum 7000792289606361"
    test_account = "Счёт 73654108430135874305"
    test_iso_date = "2024-03-11Т02:26:18.671407"

    print(mask_account_card(test_card))
    print(mask_account_card(test_account))
    print("Результат форматирования даты:", get_date(test_iso_date))
