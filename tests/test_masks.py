from src.masks import get_mask_account_number, get_mask_card_number


def test_get_mask_card_number_success():
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_get_mask_card_number_empty():
    assert get_mask_card_number("") == ""


def test_get_mask_account_success():
    assert get_mask_account_number("73654108430135874305") == "**4305"


def test_get_mask_account_empty():
    assert get_mask_account_number("") == ""
