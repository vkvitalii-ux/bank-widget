from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор, который логирует начало и конец выполнения функции."""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok"

                # Запись результата выполнения
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_message + "\n")
                else:
                    print(log_message)

                # Обязательно возвращаем результат работы функции из декоратора
                return result

            except Exception as e:

                # Формирование сообщения об ошибке по стандарту курса Skypro
                log_message = (
                    f"{func.__name__} error: {type(e).__name__}. "
                    f"Inputs: {args}, {kwargs}"
                )

                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_message + "\n")
                else:
                    print(log_message)

                # Пробрасываем ошибку дальше, чтобы тесты её видели
                raise e

        return wrapper

    return decorator
