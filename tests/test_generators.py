from typing import Dict, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "transactions, currency, expected_output",
    [
        # Корректный случай: фильтрация по USD
        (
            [
                {"id": 1, "operationAmount": {"currency": {"code": "USD"}}},
                {"id": 2, "operationAmount": {"currency": {"code": "EUR"}}},
                {"id": 3, "operationAmount": {"currency": {"code": "USD"}}},
            ],
            "USD",
            [
                {"id": 1, "operationAmount": {"currency": {"code": "USD"}}},
                {"id": 3, "operationAmount": {"currency": {"code": "USD"}}},
            ],
        ),
        # Фильтрация по валюте, которой нет в списке
        (
            [
                {"id": 1, "operationAmount": {"currency": {"code": "USD"}}},
                {"id": 2, "operationAmount": {"currency": {"code": "EUR"}}},
            ],
            "GBP",
            [],
        ),
        # Пустой список
        ([], "USD", []),
        # Список без поля operationAmount
        ([{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "PENDING"}], "USD", []),
        # Список с пустым словарём вместо корректных данных
        ([{}], "USD", []),
        # Валюта с разным регистром (должно быть чувствительно к регистру)
        (
            [
                {"id": 1, "operationAmount": {"currency": {"code": "usd"}}},
                {"id": 2, "operationAmount": {"currency": {"code": "USD"}}},
            ],
            "USD",
            [{"id": 2, "operationAmount": {"currency": {"code": "USD"}}}],
        ),
    ],
)
def test_filter_by_currency(transactions: List[Dict], currency: str, expected_output: List[Dict]) -> None:
    """Тестовая функция filter_by_currency с использованием parametrize."""
    assert list(filter_by_currency(transactions, currency)) == expected_output


@pytest.mark.parametrize(
    "transactions, expected_output",
    [
        # Корректный случай: несколько транзакций с описаниями
        (
            [
                {"id": 1, "description": "Оплата в магазине"},
                {"id": 2, "description": "Перевод другу"},
                {"id": 3, "description": "Пополнение счета"},
            ],
            ["Оплата в магазине", "Перевод другу", "Пополнение счета"],
        ),
        # Одна транзакция
        ([{"id": 1, "description": "Оплата коммунальных услуг"}], ["Оплата коммунальных услуг"]),
        # Пустой список
        ([], []),
        # Список без ключа "description" → игнорируем такие записи
        ([{"id": 1, "amount": 100}, {"id": 2, "state": "EXECUTED"}], []),
        # Частичное отсутствие ключа "description"
        (
            [
                {"id": 1, "description": "Покупка в супермаркете"},
                {"id": 2, "state": "EXECUTED"},  # нет description, игнорируем
                {"id": 3, "description": "Кафе и рестораны"},
            ],
            ["Покупка в супермаркете", "Кафе и рестораны"],
        ),
        # Пустые строки в "description" должны сохраняться
        ([{"id": 1, "description": ""}, {"id": 2, "description": "Тестовая транзакция"}], ["", "Тестовая транзакция"]),
    ],
)
def test_transaction_descriptions(transactions: List[Dict], expected_output: List[str]) -> None:
    """Тестовая функция transaction_descriptions с использованием parametrize."""
    assert list(transaction_descriptions(transactions)) == expected_output


@pytest.mark.parametrize(
    "start, end, expected_output",
    [
        # Генерация одного номера карты
        (1234567890123456, 1234567890123456, ["1234 5678 9012 3456"]),
        # Диапазон из двух номеров карт
        (1234567890123456, 1234567890123457, ["1234 5678 9012 3456", "1234 5678 9012 3457"]),
        # Генерация нескольких номеров
        (9999999999999995, 9999999999999997, ["9999 9999 9999 9995", "9999 9999 9999 9996", "9999 9999 9999 9997"]),
        # Генерация с одинаковыми start и end (один номер)
        (4000000000000000, 4000000000000000, ["4000 0000 0000 0000"]),
        # Пограничные значения
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        # Пустой диапазон (если start > end)
        (5, 3, []),
    ],
)
def test_card_number_generator(start: int, end: int, expected_output: List[str]) -> None:
    """Тестовая функция card_number_generator с использованием parametrize."""
    assert list(card_number_generator(start, end)) == expected_output
