from src.masks import get_mask_card_number, get_mask_account_number


def test_get_mask_card_number_valid():
    """Тестирование правильности маскирования стандартного номера карты"""
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_get_mask_card_number_short():
    """Проверка работы функции на нестандартной (короткой) длине номера карт"""
    assert get_mask_card_number("12345") == "12345"


def test_get_mask_card_number_empty():
    """Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты"""
    assert get_mask_card_number("") == ""


def test_get_mask_account_valid():
    """Тестирование правильности маскирования номера счета"""
    assert get_mask_account_number("73654108430135874305") == "**4305"


def test_get_mask_account_short():
    """Проверка работы функции с номерами счетов меньше ожидаемой длины"""
    assert get_mask_account_number("123") == "123"


def test_get_mask_account_empty():
    """Проверка корректной обработки пустой строки вместо номера счета"""
    assert get_mask_account_number("") == ""
