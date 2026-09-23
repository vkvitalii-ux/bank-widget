import json
import logging
import os
from typing import Any

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/utils.log", mode="w")

file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


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
        logger.error(f"Ошибка: файл {file_path} поврежден "
                     f"или сjдержит неверный формат JSON"
                     )
        return []
