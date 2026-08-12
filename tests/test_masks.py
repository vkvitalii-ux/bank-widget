from src.masks import get_mask_card_number, get_mask_account_number


def test_get_mask_card_number():
    """Тест для проверки маскирования номера карты."""
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_get_mask_account_number():
    """Тест для проверки маскирования номера счета."""
    assert get_mask_account_number("73654108430135874305") == "**4305"
