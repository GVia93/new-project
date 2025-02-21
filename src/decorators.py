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
                log_text = f"{func.__name__} ok\n"
            except Exception as e:
                log_text = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"
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
