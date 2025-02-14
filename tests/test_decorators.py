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
def test_log_success(func, args, expected, capsys):
    """Тест успешных вызовов функций"""
    result = func(*args)
    assert result == expected

    if func == divide:
        captured = capsys.readouterr()
        assert f"Function {func.__name__} was called: {expected}" in captured.out

    else:
        with open("test_log.txt") as f:
            logs = f.read()
            assert f"Function {func.__name__} was called: {expected}" in logs


# @pytest.mark.parametrize(
#     "func,args,exception",
#     [
#         (divide, (1, 0), ZeroDivisionError),
#         (add, ("a", 2), TypeError),
#         (divide, ([], {}), TypeError),
#     ],
# )
# def test_log_exception(func, args, exception, capsys):
#     """Тест вызовов функций с исключениями"""
#     with pytest.raises(exception):
#         func(*args)
#
#     if func == divide:
#         captured = capsys.readouterr()
#         assert f"Function {func.__name__} was called with args {args}" in captured.out
#         assert f"raised an exception: {exception.__name__}" in captured.out
#     else:
#         with open("test_log.txt", "r") as f:
#             logs = f.read()
#         assert f"Function {func.__name__} was called with args {args}" in logs
#         assert f"raised an exception: {exception.__name__}" in logs
