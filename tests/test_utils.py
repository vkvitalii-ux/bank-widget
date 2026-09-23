import json

from src.utils import get_financial_transactions


def test_get_transactions_success(tmp_path):
    """Тест: файл существует и содержит правильный список транзакций"""
    test_data = [{"id": 1, "state": "EXECUTED"}]
    file = tmp_path / "test.json"
    file.write_text(json.dumps(test_data))

    result = get_financial_transactions(str(file))
    assert result == test_data


def test_get_transactions_file_not_found():
    """Тест: файла не существует — возвращается пустой список []"""
    result = get_financial_transactions("non_existent_file.json")
    assert result == []


def test_get_transactions_invalid_json(tmp_path):
    """Тест: файл поврежден — возвращается пустой список []"""
    file = tmp_path / "invalid.json"
    file.write_text("{broken json...")

    result = get_financial_transactions(str(file))
    assert result == []
