from src.masks import get_mask_account_number, get_mask_card_number


def mask_account_card(info: str) -> str:
    """Функция маскирует номер карты или счёта в зависимости от входных данных."""
    if not info:
        return ""

    parts = info.split()
    name = " ".join(parts[:-1])
    number = parts[-1]

    if "Счёт" in name:
        return f"{name} {get_mask_account_number(number)}"
    else:
        return f"{name} {get_mask_card_number(number)}"
