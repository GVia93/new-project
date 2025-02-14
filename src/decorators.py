import functools


def log(filename=None):
    """
    Декоратор для логирования вызовов функций и обработке исключений.
    Необязательный аргумент "filename", который определяет имя файла, для записи логов.
    Если "filename" не задан, то логи выводятся в консоль.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_text = f"Function {func.__name__} was called: {result}"
            except Exception as e:
                log_text = (
                    f"Function {func.__name__} was called with args {args} and kwargs {kwargs} raised an exception: {e}"
                )
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_text)
                else:
                    print(log_text)
                raise

            if filename:
                with open(filename, "a") as f:
                    f.write(log_text)
            else:
                print(log_text)

            return result

        return wrapper

    return decorator
