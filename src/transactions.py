import csv

import pandas as pd


def transactions_csv(filename: str) -> list[dict[str, str]]:
    """
    Функция для считывания финансовых операций из CSV.

    :param filename: Имя CSV-файла.
    :return: Список словарей, где каждый словарь отдельная транзакция.
    """
    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            transactions_list = [row for row in reader]
            return transactions_list
    except FileNotFoundError as e:
        print(f"Файл не найден: {e}")
    except csv.Error as e:
        print(f"Ошибка чтения файла CSV: {e}")

    return []


def transactions_excel(filename: str) -> list[dict[str, str]]:
    """
    Функция для считывания финансовых операций из Excel.

    :param filename: Имя Excel-файла.
    :return: Список словарей, где каждый словарь отдельная транзакция.
    """
    try:
        df = pd.read_excel(filename)
        transactions_list = df.to_dict(orient="records")
        return transactions_list
    except FileNotFoundError as e:
        print(f"Файл не найден: {e}")

    return []
