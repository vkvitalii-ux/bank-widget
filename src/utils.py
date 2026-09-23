import json
import os

import logging
logging.basicConfig(filename="logs/utils.log", filemode="w",
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

from typing import Any


def get_financial_transactions(file_path: str) -> list[dict[str, Any]]:
    """
    Принимает путь до JSON-файла и возвращает список транзакций.
    Если файл пустой, поврежден или отсутствует, возвращает пустой список.
    """

    logger.info(f"Запрос на чтение финансовых транзакций из {file_path}")
    if not os.path.exists(file_path):
        logger.warning(f"Стоп '{file_path}' файла на диске нет.")
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, FileNotFoundError):
        logger.error(f"Ошибка: файл {file_path} поврежден или сдержит неверный формат JSON")
        return []
