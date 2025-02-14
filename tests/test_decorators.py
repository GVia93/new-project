import pytest

from src.decorators import log


@log(filename="test_log.txt")
def add(a, b):
    return a + b


@log(filename=None)
def divide(a, b):
    return a / b


@pytest.mark.parametrize(
    "func,args,expected",
    [
        (add, (2, 3), 5),
        (add, (-1, 1), 0),
        (divide, (6, 2), 3),
    ],
)
def test_log_success(func, args, expected):
    """Тест успешных вызовов функций"""
    result = func(*args)
    assert result == expected


@pytest.mark.parametrize(
    "func,args,exception",
    [
        (divide, (1, 0), ZeroDivisionError),
        (add, ('a', 2), TypeError),
        (divide, ([], {}), TypeError),
    ],
)
def test_log_exception(func, args, exception):
    """Тест вызовов функций с исключениями"""
    with pytest.raises(exception):
        func(*args)
