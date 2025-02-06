from typing import Dict, List
from datetime import datetime


def sort_by_date(list_info: List[Dict[str, str]], descending: bool = True) -> List[Dict[str, str]]:
    """
    Сортирует список словарей по ключу 'date'.

    :param list_info: Список словарей, содержащих ключ 'date'.
    :param descending: Указывает порядок сортировки (по умолчанию True - по убыванию).
    :return: Новый список, отсортированный по ключу 'date'.
    """

    def parse_date(item):
        try:
            return datetime.fromisoformat(item.get('date', ''))
        except ValueError:
            return datetime.min

    return sorted(list_info, key=parse_date, reverse=descending)


def filter_by_state(list_info: List[Dict[str, str]], state: str = 'EXECUTED') -> List[Dict[str, str]]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param list_info: Список словарей.
    :param state: Значение для фильтрации (по умолчанию 'EXECUTED').
    :return: Новый список словарей с указанным значением ключа 'state'.
    """
    return [item for item in list_info if item.get('state') == state]
