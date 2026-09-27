import logging

import pandas as pd

logger = logging.getLogger(__name__)


def read_csv_financial_transactions(file_path: str) -> list:
    """Функция считывает финансовые операции из CSV-файла."""
    logger.info("Начало чтения CSV-файла")
    df = pd.read_csv(file_path, sep=';')
    print(df.shape)
    return df.to_dict(orient='records')


def read_excel_financial_transactions(file_path: str) -> list:
    """Функция считывает финансовые операции из EXCEL-файла."""
    logger.info("Начало чтения EXCEL-файла")
    df = pd.read_excel(file_path)
    print(df.shape)
    return df.to_dict(orient='records')


if __name__ == "__main__":
    print(read_csv_financial_transactions("../data/transactions.csv"))
    print(read_excel_financial_transactions("../data/transactions_excel.xlsx"))
