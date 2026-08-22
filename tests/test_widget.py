import pytest
from src.widget import mask_account_card, get_date


# =====================================================================
# ТЕСТЫ ДЛЯ ФУНКЦИИ mask_account_card
# =====================================================================

def test_mask_account_card_card_type():
    """Проверка, что функция корректно распознает карту и применяет маску карты."""
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"


def test_mask_account_card_account_type():
    """Проверка, что функция корректно распознает счет и применяет маску счета."""
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"


@pytest.mark.parametrize(
    "info_string, expected",
    [
        ("Maestro 1596237415962374", "Maestro 1596 23** **** 2374"),
        ("MasterCard 7000792289606361", "MasterCard 7000 79** **** 6361"),
        ("Visa Classic 1111222233334444", "Visa Classic 1111 22** **** 4444"),
        ("Счёт 12345678901234567890", "Счёт **7890"),
    ]
)
def test_mask_account_card_parametrized(info_string, expected):
    """Параметризованные тесты с разными типами карт и счетов для проверки универсальности."""
    assert mask_account_card(info_string) == expected


@pytest.mark.parametrize(
    "invalid_input, expected",
    [
        ("НекорректнаяСтрокаБезНомера", "НекорректнаяСтрокаБезНомера"),
        ("12345", "12345"),
        ("Visa 123", "Visa 123"), # Слишком короткий номер
    ]
)
def test_mask_account_card_invalid_data(invalid_input, expected):
    """Тестирование функции на обработку некорректных входных данных."""
    assert mask_account_card(invalid_input) == expected


# =====================================================================
# ТЕСТЫ ДЛЯ ФУНКЦИИ get_date
# =====================================================================

def test_get_date_valid():
    """Тестирование правильности преобразования стандартной даты."""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2026-12-31T23:59:59", "31.12.2026"),
        ("2000-01-01T00:00:00.000", "01.01.2000"),
    ]
)
def test_get_date_formats(date_str, expected):
    """Проверка работы функции на различных входных форматах даты."""
    assert get_date(date_str) == expected


@pytest.mark.parametrize(
    "empty_input",
    ["", " "]
)
def test_get_date_empty(empty_input):
    """Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата."""
    assert get_date(empty_input) == ""
