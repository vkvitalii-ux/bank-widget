def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтрует список словарей по значению ключа 'state'."""
    filtered_list = []
    for item in data:
        if item.get("state") == state:
            filtered_list.append(item)
    return filtered_list


def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    """Сортирует список словарей по дате от большей к меньшей
    (по умолчанию)."""
    sorted_list = sorted(
        data,
        key=lambda item: item.get("date", ""),
        reverse=reverse
    )
    return sorted_list
