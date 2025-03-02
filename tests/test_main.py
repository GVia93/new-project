import pytest
from src.processing import filter_by_description, filter_by_state
from src.widget import get_date, mask_account_card


@pytest.fixture
def transactions():
    return [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        },
    ]


def test_filter_by_state(transactions):
    """
    Тест для фильтрации по статусу.
    """
    filtered = filter_by_state(transactions, "EXECUTED")
    assert len(filtered) == 2


def test_filter_by_description(transactions):
    """
    Тест для фильтрации по описанию.
    """
    filtered = filter_by_description(transactions, "Перевод организации")
    assert len(filtered) == 1


def test_mask_account_card(transactions):
    """
    Тест для маскировки номера карты и счета.
    """
    masked_card = mask_account_card(transactions[0]["from"])
    assert masked_card == "MasterCard 7158 30** **** 6758"

    masked_account = mask_account_card(transactions[0]["to"])
    assert masked_account == "Счет **5560"


def test_get_date(transactions):
    """
    Тест для форматирования даты
    """
    date_str = get_date(transactions[0]["date"])
    assert date_str == "03.07.2019"
