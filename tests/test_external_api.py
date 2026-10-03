from unittest.mock import patch, Mock
from src.external_api import convert_transaction_amount


def test_convert_rub():
    """Тест: если валюта RUB, функция сразу возвращает сумму без запросов"""
    transaction = {
        "operationAmount": {
            "amount": "150.50",
            "currency": {"code": "RUB"}
        }
    }
    result = convert_transaction_amount(transaction)
    assert result == 150.50


@patch('requests.get')
def test_convert_usd_success(mock_get):
    """Тест: симуляция успешного ответа API для валюты USD"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 7500.0}
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "USD"}
        }
    }

    result = convert_transaction_amount(transaction)
    assert result == 7500.0
    mock_get.assert_called_once()
