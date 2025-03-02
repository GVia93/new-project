import csv
import json
import logging

import pandas as pd

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/utils.log")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def load_transactions_json(file_path: str) -> list[dict[str, str]]:
    """
    Загружает данные о финансовых транзакциях из JSON-файла.

    :param file_path: Имя JSON-файла.
    :return: Список словарей, где каждый словарь отдельная транзакция.
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


def load_transactions_csv(file_path: str) -> list[dict[str, str]]:
    """
    Функция для считывания финансовых операций из CSV.

    :param file_path: Имя CSV-файла.
    :return: Список словарей, где каждый словарь отдельная транзакция.
    """
    try:
        with open(file_path, mode="r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            transactions = [row for row in reader]
            return transactions
    except FileNotFoundError as e:
        logger.error(f"Файл не найден: {e}")
    except csv.Error as e:
        logger.error(f"Ошибка чтения файла CSV: {e}")

    return []


def load_transactions_excel(file_path: str) -> list[dict[str, str]]:
    """
    Функция для считывания финансовых операций из Excel.

    :param file_path: Имя Excel-файла.
    :return: Список словарей, где каждый словарь отдельная транзакция.
    """
    try:
        df = pd.read_excel(file_path)
        transactions = df.to_dict(orient="records")
        return transactions
    except FileNotFoundError as e:
        logger.error(f"Файл не найден: {e}")

    return []
