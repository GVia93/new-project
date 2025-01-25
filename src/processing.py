from typing import Dict, List


def sort_by_date(list_info: List[Dict[str, str]], descending: bool = True) -> List[Dict[str, str]]:
    """
    Сортирует список словарей по ключу 'date'

    :param list_info: Список словарей, где есть ключ 'date'.
    :param descending: Указывает порядок сортировки (по умолчанию True - по убыванию).
    :return: Новый список, отсортированный по ключу 'date'.
    """
    sorted_list = sorted(list_info, key=lambda x: x['date'], reverse=descending)
    return sorted_list


def filter_by_state(list_info: List[Dict[str, str]], state: str = 'EXECUTED') -> List[Dict[str, str]]:
    """
    Фильтр списка словарей по значению ключа 'state'

    :param list_info: Список словарей.
    :param state: Значение для фильтрации (по умолчанию 'EXECUTED')
    :return: Новый список словарей с указанным значением ключа 'state'.
    """
    filtered_list = []
    for item in list_info:
        if item.get('state') == state:
            filtered_list.append(item)
    return filtered_list
