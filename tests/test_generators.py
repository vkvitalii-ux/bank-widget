import pytest

from src.generators import (
    card_number_generator, filter_by_currency, transaction_descriptions
)


@pytest.fixture
def sample_transactions():
    """Возвращает тестовый список транзакций для проверки генераторов."""
    return [
        {
            "id": 939719570,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Перевод организации",
        },
        {
            "id": 142264268,
            "operationAmount": {"currency": {"code": "RUB"}},
            "description": "Перевод со счета на счет",
        },
        {
            "id": 441945886,
            "operationAmount": {"currency": {"code": "RUB"}},
        },
    ]


def test_filter_by_currency(sample_transactions):
    """Тестирует фильтрацию транзакций по заданной валюте."""
    usd = list(filter_by_currency(sample_transactions, "USD"))
    assert len(usd) == 1
    assert usd[0]["id"] == 939719570


def test_transaction_descriptions(sample_transactions):
    """Тестирует генерацию списка описаний для транзакций."""
    descriptions = list(transaction_descriptions(sample_transactions))
    assert descriptions == [
        "Перевод организации",
        "Перевод со счета на счет",
        "",
    ]


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 2, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
        (999, 1000, ["0000 0000 0000 0999", "0000 0000 0000 1000"]),
    ],
)
def test_card_number_generator(start, stop, expected):
    """Тестирует генератор номеров карт на корректность диапозонов."""
    generator = card_number_generator(start, stop)
    assert list(generator) == expected
