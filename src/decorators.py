def log(filename="log.txt"):
    """
    Декоратор для логирования вызовов функций и обработке исключений.

    Записывает в указанный файл информацию о вызове функции, включая её имя, аргументы,
    ключевые аргументы, и результат выполнения или информацию об исключении, если оно возникло.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                with open(filename, "a") as f:
                    f.write(f"Function {func.__name__} was called: {result}\n")
            except Exception as e:
                with open(filename, "a") as f:
                    f.write(
                        f"Function {func.__name__} was called with args {args} and kwargs {kwargs} raised an exception: {e}\n"
                    )
                    raise
            return result

        return wrapper

    return decorator
