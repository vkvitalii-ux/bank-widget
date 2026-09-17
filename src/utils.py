import json
import os
from typing import Any


def get_financial_transactions(file_path: str) -> list[dict[str, Any]]:
    """
    Принимает путь до JSON-файла и возвращает список транзакций.
    Если файл пустой, поврежден или отсутствует, возвращает пустой список.
    """
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, FileNotFoundError):
        return []
