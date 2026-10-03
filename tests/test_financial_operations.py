from src.financial_operations import read_csv_financial_transactions, read_excel_financial_transactions
from unittest.mock import patch
import pandas as pd


@patch('pandas.read_csv')
def test_read_csv_financial_transactions(mock_read_csv):
    expected_result = [{"id": 123, "state": "EXECUTED", "amount": 100.0}]
    mock_read_csv.return_value = pd.DataFrame(expected_result)
    result = read_csv_financial_transactions("test.csv")
    assert result == expected_result


@patch('pandas.read_excel')
def test_read_excel_financial_transactions(mock_read_excel):
    expected_result = [{"id": 123, "state": "EXECUTED", "amount": 100.0}]
    mock_read_excel.return_value = pd.DataFrame(expected_result)
    result = read_excel_financial_transactions("test.excel.xlsx")
    assert result == expected_result
