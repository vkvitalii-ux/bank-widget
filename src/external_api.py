import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("EXCHANGE_API_KEY")


def convert_transaction_amount(transaction: dict) -> float:
    """
    Принимает словарь с одной транзакцией и возвращает сумму в рублях (float).
    """

    # Достаем сумму и код валюты из структуры JSON
    operation_amount = transaction.get("operationAmount", {})
    amount_str = operation_amount.get("amount", 0.0)
    currency_info = operation_amount.get("currency", {})
    currency_code = currency_info.get("code", "RUB")

    amount = float(amount_str)

    # Если валюта изначально в рублях, конвертация не нужна
    if currency_code == "RUB":
        return amount

    # Если валюта USD или EUR, делаем запрос к внешнему сервису курсов
    url = f"https://apilayer.com{currency_code}&amount={amount}"
    headers = {"apikey": API_KEY}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return float(data.get("result", 0.0))

    return 0.0
