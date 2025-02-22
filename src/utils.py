import json
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="logs/utils.log",  # Запись логов в файл
    filemode="w",  # Перезапись файла при каждом запуске
)
logger = logging.getLogger(__name__)


def load_transactions(file_path: str) -> list:
    """
    Загружает данные о финансовых транзакциях из JSON-файла.

    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            transactions = json.load(file)
    except json.JSONDecodeError as e:
        logger.error(f"Некорректный JSON в файле {file_path}: {e}")
        return []
    except FileNotFoundError as e:
        logger.error(f"Файл не найден: {e}")
        return []

    if not isinstance(transactions, list):
        logger.error(f"Файл {file_path} должен содержать список транзакций.")
        return []

    logger.info("Загрузка данных о финансовых транзакциях выполнена.")
    return transactions
