from src.widget import mask_account_card, get_date

# Тест пустой строки или строки из пробелов
def test_mask_account_card_empty():
    assert mask_account_card("") == ""
    assert mask_account_card(" ") == ""

# Тест строки, где меньше двух слов
def test_mask_account_card_short():
    assert mask_account_card("Visa") == "Visa"

# Тест для Счета
def test_mask_account_card_account():
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"
    assert mask_account_card("счёт 73654108430135874305") == "счёт **4305"
    assert mask_account_card("Visa 7365410843013587") == "Visa 7365 41** **** 3587"
# Тест пустой даты
def test_get_date_empty():
    assert get_date("") == ""
    assert get_date("2024-03") == ""

def test_get_date_valid():
    """Тест проверяет, что функция get_data правильно переводит формат даты"""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_mask_account_card_empty_string():
    """Тест проверяет работу маски, если ей передали пустую строку"""
    assert mask_account_card("") == ""
