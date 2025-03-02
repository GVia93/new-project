from typing import Any, Dict, List

import pytest

from src.processing import count_transactions_by_category, filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "input_list, descending, expected_output",
    [
        # Правильная сортировка по дате (по убыванию)
        (
            [
                {"id": 1, "date": "2024-03-11T02:26:18.671407"},
                {"id": 2, "date": "2023-12-01T14:50:00.123456"},
                {"id": 3, "date": "2024-01-15T12:10:30.123456"},
            ],
            True,
            [
                {"id": 1, "date": "2024-03-11T02:26:18.671407"},
                {"id": 3, "date": "2024-01-15T12:10:30.123456"},
                {"id": 2, "date": "2023-12-01T14:50:00.123456"},
            ],
        ),
        # Сортировка по возрастанию
        (
            [
                {"id": 1, "date": "2024-03-11T02:26:18.671407"},
                {"id": 2, "date": "2023-12-01T14:50:00.123456"},
                {"id": 3, "date": "2024-01-15T12:10:30.123456"},
            ],
            False,
            [
                {"id": 2, "date": "2023-12-01T14:50:00.123456"},
                {"id": 3, "date": "2024-01-15T12:10:30.123456"},
                {"id": 1, "date": "2024-03-11T02:26:18.671407"},
            ],
        ),
        # Пустой список
        ([], True, []),
        # Список с отсутствующим ключом 'date' (ничего не изменится)
        ([{"id": 1}, {"id": 2}, {"id": 3}], True, [{"id": 1}, {"id": 2}, {"id": 3}]),
        # Некорректный формат даты (например, неправильно указанный ключ)
        (
            [{"id": 1, "date": "invalid_date"}, {"id": 2, "date": "2023-12-01T14:50:00.123456"}],
            True,
            [{"id": 2, "date": "2023-12-01T14:50:00.123456"}, {"id": 1, "date": "invalid_date"}],
        ),
    ],
)
def test_sort_by_date(
    input_list: List[Dict[str, Any]], descending: bool, expected_output: List[Dict[str, Any]]
) -> None:
    """Тестовая функция sort_by_date с использованием parametrize."""
    assert sort_by_date(input_list, descending) == expected_output


@pytest.mark.parametrize(
    "input_list, state, expected_output",
    [
        # Фильтрация по статусу EXECUTED
        (
            [{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "PENDING"}, {"id": 3, "state": "EXECUTED"}],
            "EXECUTED",
            [{"id": 1, "state": "EXECUTED"}, {"id": 3, "state": "EXECUTED"}],
        ),
        # Фильтрация по статусу PENDING
        ([{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "PENDING"}], "PENDING", [{"id": 2, "state": "PENDING"}]),
        # Пустой список
        ([], "EXECUTED", []),
        # Список без ключа 'state'
        ([{"id": 1, "amount": 100}, {"id": 2, "amount": 200}], "EXECUTED", []),
        # Некорректные данные в поле state
        ([{"id": 1, "state": None}, {"id": 2, "state": "EXECUTED"}], "EXECUTED", [{"id": 2, "state": "EXECUTED"}]),
        # Список с несуществующим состоянием
        ([{"id": 1, "state": "EXECUTED"}, {"id": 2, "state": "PENDING"}], "FAILED", []),
    ],
)
def test_filter_by_state(input_list: List[Dict[str, Any]], state: str, expected_output: List[Dict[str, Any]]) -> None:
    """Тестовая функция fiter_by_state с использованием parametrize."""
    assert filter_by_state(input_list, state) == expected_output


@pytest.fixture
def sample_transactions():
    return [
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
        {"description": "Перевод с карты на карту"},
    ]


@pytest.fixture
def sample_categories():
    return ["Перевод организации", "Открытие вклада", "Перевод с карты на карту"]


def test_count_transactions_by_category(sample_transactions, sample_categories):
    """Тестирует функцию count_transactions_by_category на корректность подсчета транзакций по категориям."""
    expected_result = {
        "Перевод организации": 1,
        "Открытие вклада": 1,
        "Перевод с карты на карту": 1,
    }
    result = count_transactions_by_category(sample_transactions, sample_categories)
    assert result == expected_result
