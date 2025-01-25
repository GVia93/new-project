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
