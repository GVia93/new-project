import csv
from typing import Any

import pandas as pd


def transactions_csv(filename: str) -> list[dict[Any, str]]:
    """
    Функция для считывания финансовых операций из CSV.

    :param filename: Имя CSV-файла.
    :return: Список словарей, где каждый словарь отдельная транзакция.
    """
    with open(filename, mode="r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        transactions_list = [row for row in reader]

    return transactions_list


def transactions_excel(filename: str) -> list[dict[Any, str]]:
    """
    Функция для считывания финансовых операций из Excel.

    :param filename: Имя CSV-файла.
    :return: Список словарей, где каждый словарь отдельная транзакция.
    """
    df = pd.read_excel(filename)
    transactions_list = df.to_dict(orient="records")
    return transactions_list
