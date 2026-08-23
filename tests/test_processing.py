import pytest
from src.processing import filter_by_state, sort_by_date


# Тестовые данные (общие для тестов)
@pytest.fixture
def sample_data():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-03-11T12:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2024-03-12T15:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2024-03-10T09:00:00"},
    ]


# === ТЕСТЫ ДЛЯ ФУНКЦИИ filter_by_state ===


# 1. Параметризация для разных статусов + базовая фильтрация
@pytest.mark.parametrize(
    "state, expected_ids",
    [
        ("EXECUTED", [1, 3]),
        ("CANCELED", [2]),
    ],
)
def test_filter_by_state_valid(sample_data, state, expected_ids):
    """Тестирование фильтрации по заданному статусу state"""
    result = filter_by_state(sample_data, state)
    assert [item["id"] for item in result] == expected_ids


# 2. Проверка работы при отсутствии словарей с указанным статусом
def test_filter_by_state_empty_result(sample_data):
    """Проверка работы, когда словарей с таким статусом нет в списке"""
    result = filter_by_state(sample_data, "PENDING")
    assert result == []


# === ТЕСТЫ ДЛЯ ФУНКЦИИ sort_by_date ===


# 1. Сортировка по убыванию и возрастанию
def test_sort_by_date_order(sample_data):
    """Тестирование сортировки по датам в порядке убывания и возрастания"""
    # По убыванию (сначала самые свежие)
    result_desc = sort_by_date(sample_data)
    # или reverse=True, смотря как в вашей функции по умолчанию
    assert [item["id"] for item in result_desc] == [2, 1, 3]

    # По возрастанию
    result_asc = sort_by_date(sample_data, reverse=False)
    # или наоборот, подстройте под аргументы вашей функции
    assert [item["id"] for item in result_asc] == [3, 1, 2]


# 2. Корректность сортировки при одинаковых датах
def test_sort_by_date_identical():
    """Проверка корректности сортировки при одинаковых датах"""
    data = [
        {"id": 1, "date": "2024-03-11T12:00:00"},
        {"id": 2, "date": "2024-03-11T12:00:00"},
    ]
    # При одинаковых датах порядок элементов не должен ломать программу
    result = sort_by_date(data)
    assert len(result) == 2


# 3. Тест на некорректный формат дат
def test_sort_by_date_invalid_format():
    """Тесты на работу функции с некорректными форматами дат"""
    data = [
        {"id": 1, "date": "invalid-date"},
        {"id": 2, "date": "2024-03-11"},
    ]
    # Здесь пишется поведение вашей функции: возвращает пустой список,
    # игнорирует или падает с ошибкой. Например, если она должна пропускать:
    try:
        sort_by_date(data)
    except Exception as e:
        pytest.fail(f"Функция упала с ошибкой {e} при некорректной дате")