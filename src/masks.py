import logging

logger = logging.getLogger(__name__)

def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует номер банковской карты."""
    logger.info(f"Начало маскирования карты. Исходный номер: {card_number}")
    if not card_number or len(card_number) < 16:
        logger.warning(f"Передан некорректный номер карты: {card_number}. Длина должна быть 16 символов.")
        return card_number

    masked = (
            card_number[:4] + " " + card_number[4:6] + "** **** "
            + card_number[-4:]
    )
    logger.info(f"Номер карты успешно замаскирован: {masked}")
    return masked


def get_mask_account_number(account_number: str) -> str:
    """Функция маскирует номер банковского счета."""
    logger.info(f"Начало маскирования счета. Исходный номер: {account_number}")
    if not account_number or len(account_number) < 4:
        logger.warning(f"Передан некорректный номер счета: {account_number}. Длина должна быть 4 символа.")
        return account_number

    masked_account = "**" + account_number[-4:]
    logger.info(f"Номер счета успешно замаскирован: {masked_account}")
    return masked_account
