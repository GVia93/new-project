import logging


def setup_logger():
    """
    Основная конфигурация logging
    """
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                        filename="logs/application.log",  # Запись логов в файл
                        filemode="w", )  # Перезапись файла при каждом запуске
    return logging.getLogger()
