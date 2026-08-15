def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтрует список словарей по значению ключа 'state'."""
    filtered_list = []
    for item in data:
        if item.get("state") == state:
            filtered_list.append(item)
    return filtered_list
