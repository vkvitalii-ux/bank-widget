from src.widget import get_date, mask_account_card


def test_mask_card_visa():
    """Тест для маскирования карты Visa."""
    card_info = "Visa 7000792289606361"
    expected = "Visa 7000 79** **** 6361"
    assert mask_account_card(card_info) == expected


def test_mask_account():
    """Тест для счета."""
    account_info = "Счет 7365410830135874305"
    expected = "Счет **4305"
    assert mask_account_card(account_info) == expected


def test_mask_account_card_account():
    # Тестируем счет, чтобы зайти
    # в нужное условие функции
    account_info = "Счет 7365410830135874305"
    assert "Счет" in mask_account_card(account_info)


def test_mask_account_card_single_word():
    # Тестируем условие, если
    # len(parts) имеет другую длину
    assert mask_account_card("Mastercard") == "Mastercard"


def test_get_date_valid():
    """Тест успешного форматирования даты."""
    # Тестируем функцию get_date (строка)
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_mask_account_card_empty_string():
    # Тестируем передачу пустой строки
    assert mask_account_card("") == ""
    assert mask_account_card("  ") == ""
