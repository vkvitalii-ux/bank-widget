import os

from src.decorators import log


def test_log_to_console_success(capsys):
    """Тест успешного логирования в консоль."""

    @log()
    def add(x, y):
        return x + y

    assert add(2, 3) == 5
    captured = capsys.readouterr()
    assert captured.out.strip() == "add ok"


def test_log_to_console_error(capsys):
    """Тест логирования ошибки в консоль."""

    @log()
    def divide(x, y):
        return x / y

    try:
        divide(1, 0)
    except ZeroDivisionError:
        pass

    captured = capsys.readouterr()
    expected_msg = "divide error: ZeroDivisionError. Inputs: (1, 0), {}"
    assert expected_msg in captured.out


def test_log_to_file_success():
    """Тест успешного логирования в файл."""
    test_file = "test_success.log"

    @log(filename=test_file)
    def greet(name):
        return f"Hello, {name}"

    assert greet("Alice") == "Hello, Alice"

    with open(test_file, "r", encoding="utf-8") as f:
        log_content = f.read().strip()

    assert log_content == "greet ok"

    if os.path.exists(test_file):
        os.remove(test_file)


def test_log_to_file_error():
    """Тест логирования ошибки в файл."""
    test_file = "test_error.log"

    @log(filename=test_file)
    def cause_error():
        raise ValueError("Some error")

    try:
        cause_error()
    except ValueError:
        pass

    with open(test_file, "r", encoding="utf-8") as f:
        log_content = f.read().strip()

    assert "cause_error error: ValueError. Inputs: (), {}" in log_content

    if os.path.exists(test_file):
        os.remove(test_file)
