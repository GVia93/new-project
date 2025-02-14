import pytest

from src.decorators import log


@log(filename="test_log.txt")
def add(a, b):
    return a + b


@log(filename=None)
def divide(a, b):
    return a / b


@pytest.mark.parametrize(
    "func,args,expected,log_text",
    [
        (add, (2, 3), 5, "add ok\n"),
        (add, (-1, 1), 0, "add ok\n"),
        (divide, (6, 2), 3, "divide ok\n"),
    ],
)
def test_log_success(func, args, expected, capsys, log_text):
    """Тест успешных вызовов функций"""
    result = func(*args)
    assert result == expected

    if func == divide:
        captured = capsys.readouterr()
        assert log_text in captured.out

    else:
        with open("test_log.txt") as f:
            logs = f.read()
            assert log_text in logs


@pytest.mark.parametrize(
    "func,args,exception,log_text",
    [
        (divide, (1, 0), ZeroDivisionError, "divide error: ZeroDivisionError. Inputs: (1, 0), {}\n"),
        (add, ("a", 2), TypeError, "add error: TypeError. Inputs: ('a', 2), {}\n"),
    ],
)
def test_log_exception(func, args, exception, capsys, log_text):
    """Тест вызовов функций с исключениями"""
    with pytest.raises(exception):
        func(*args)

    if func == divide:
        captured = capsys.readouterr()
        assert log_text in captured.out
    else:
        with open("test_log.txt", "r") as f:
            logs = f.read()
        assert log_text in logs
