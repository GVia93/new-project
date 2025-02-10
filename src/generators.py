from typing import Dict, Iterator, List


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    """
    Фильтрует список транзакций по указанной валюте.

    :param transactions: Список словарей, представляющих транзакции.
    :param currency: Валюта, по которой фильтруются транзакции (например, 'USD').
    :return: Итератор с отфильтрованными транзакциями.
    """
    return (
        transactions
        for transactions in transactions
        if transactions.get("operationAmount", {}).get("currency", {}).get("code") == currency
    )


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Генератор, который возвращает описание каждой транзакции.

    :param transactions: Список словарей с транзакциями.
    :return: Итератор, возвращающий описание каждой операции.
    """
    return (transaction["description"] for transaction in transactions if "description" in transaction)


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX.

    :param start: Начальный номер карты (от 1 до 9999999999999999).
    :param end: Конечный номер карты (до 9999999999999999).
    :return: Итератор строк с номерами карт в формате XXXX XXXX XXXX XXXX.
    """
    return (" ".join(f"{num:016d}"[i : i + 4] for i in range(0, 16, 4)) for num in range(start, end + 1))
