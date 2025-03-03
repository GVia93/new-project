import re
from collections import defaultdict
from datetime import datetime
from typing import Any, Dict, List


def sort_by_date(list_info: List[Dict[str, str]], descending: bool = True) -> List[Dict[str, str]]:
    """
    Сортирует список словарей по ключу 'date'.

    :param list_info: Список словарей, содержащих ключ 'date'.
    :param descending: Указывает порядок сортировки (по умолчанию True - по убыванию).
    :return: Новый список, отсортированный по ключу 'date'.
    """

    def parse_date(item: Dict[str, Any]) -> datetime:
        try:
            return datetime.fromisoformat(item.get("date", ""))
        except ValueError:
            return datetime.min

    return sorted(list_info, key=parse_date, reverse=descending)


def filter_by_state(list_info: List[Dict[str, str]], state: str = "EXECUTED") -> List[Dict[str, str]]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param list_info: Список словарей.
    :param state: Значение для фильтрации (по умолчанию 'EXECUTED').
    :return: Новый список словарей с указанным значением ключа 'state'.
    """
    return [item for item in list_info if item.get("state") == state]


def filter_by_description(transactions: list[dict], search_string: str) -> list[dict]:
    """
    Фильтрует список транзакций по строке в описании.

    :param transactions: Список словарей с транзакциями.
    :param search_string: Строка для поиска в описании.
    :return: Список транзакций, в описании которых найдена строка.
    """
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction.get("description", ""))]


def count_transactions_by_category(transactions: list[dict], categories: list[str]) -> dict[str, int]:
    """
    Подсчитывает количество операций в каждой категории.

    :param transactions: Список словарей с транзакциями.
    :param categories: Список категорий для подсчета.
    :return: Словарь с количеством операций по каждой категории.
    """
    category_counts = defaultdict(int)
    for transaction in transactions:
        description = transaction.get("description", "").lower()
        for category in categories:
            if category.lower() in description:
                category_counts[category] += 1
    return dict(category_counts)
