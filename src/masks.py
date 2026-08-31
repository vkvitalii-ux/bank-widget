def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует номер банковской карты."""
    if not card_number or len(card_number) < 16:
        return card_number

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account_number(account_number: str) -> str:
    """Функция маскирует номер банковского счета."""
    if not account_number or len(account_number) < 4:
        return account_number

    return f"**{account_number[-4:]}"
