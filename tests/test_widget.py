from src.widget import get_date, mask_account_card


def test_masks_card_visa():
    """Тестирует маскирование номера карты Visa."""
    card = "Visa Platinum 7000792289606361"
    expected = "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card(card) == expected


def test_masks_account():
    """Тестирует маскирование номера счета."""
    account = "Счет 73654108430135874305"
    expected = "Счет **4305"
    assert mask_account_card(account) == expected


def test_get_date_success():
    """Тестирует правильную конвертацию даты."""
    date_str = "2018-07-11T02:26:18.671407"
    assert get_date(date_str) == "11.07.2018"


def test_get_date_valid():
    """Тестируем правильную конвертацию даты"""
    date_str = "2024-03-11T02:26:18.671407"
    assert get_date(date_str) == "11.03.2024"


def test_get_date_empty():
    """Тестируем пустую строку даты"""
    assert get_date("") == ""


def test_mask_account_card_empty():
    """Тестируем пустую строку в маскировании"""
    assert mask_account_card("") == ""
    assert mask_account_card("Счет") == "Счет"
