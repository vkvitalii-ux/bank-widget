from typing import Iterable, Iterator


def filter_by_currency(
        transactions: Iterable[dict],
        currency: str
) -> Iterator[dict]:
    """Фильтрует транзакции по заданной валюте."""
    for transaction in transactions:
        operation_amount = transaction.get("operationAmount", {})
        if operation_amount:
            currency_info = operation_amount.get("currency", {})
            if currency_info and currency_info.get("code") == currency:
                yield transaction


def transaction_descriptions(
        transactions: Iterable[dict]
) -> Iterator[str]:
    """Возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(
        start: int,
        stop: int
) -> Iterator[str]:
    """Генерирует номера карт в формате XXXX XXXX XXXX XXXX."""
    for number in range(start, stop + 1):
        card_str = f"{number:016d}"
        part1 = f"{card_str[0:4]} {card_str[4:8]}"
        part2 = f"{card_str[8:12]} {card_str[12:16]}"
        yield f"{part1} {part2}"
