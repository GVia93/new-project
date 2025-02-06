from typing import Optional

import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "account_card, expected_output",
    [
        # Корректные данные: карты
        ("Visa Platinum 1234567890123456", "Visa Platinum 1234 56** **** 3456"),
        ("Mastercard 5432112345678901", "Mastercard 5432 11** **** 8901"),
        ("American Express 375987654321001", "American Express 3759 87** **** 001"),
        ("Maestro 6759000000000000000", "Maestro 6759 00** **** 0000 000"),
        # Корректные данные: счета
        ("Счет 12345678901234567890", "Счет **7890"),
        # Корректные данные с дефисами
        ("Visa Platinum 1234-5678-9012-3456", "Visa Platinum 1234 56** **** 3456"),
        ("Счет 1234-5678-9012-3456-7890", "Счет **7890"),
        # Некорректные данные
        ("Visa Platinum ABCD567890123456", "Не корректные данные"),  # Буквы в номере карты
        ("Счет 1234ABCD5678EFGH9012", "Не корректные данные"),  # Буквы в номере счета
        ("Visa 12345", "Не корректные данные"),  # Слишком короткий номер
        ("Mastercard 123456789012345678901", "Не корректные данные"),  # Слишком длинный номер
        ("", "Не корректные данные"),  # Пустая строка
        ("Счет", "Не корректные данные"),  # Только "Счет" без номера
        ("Visa Platinum", "Не корректные данные"),  # Только название карты
        ("1234567890123456", "Не корректные данные"),  # Отсутствует название карты или "Счет"
    ],
)
def test_mask_account_card(account_card: str, expected_output: str) -> None:
    """Тестовая функция mask_account_card с использованием parametrize."""
    assert mask_account_card(account_card) == expected_output


@pytest.mark.parametrize(
    "date_str, expected, raises_exception",
    [
        # Корректные даты
        ("2024-03-11T02:26:18.671407", "11.03.2024", False),
        ("2000-01-01T00:00:00.000000", "01.01.2000", False),
        ("1999-12-31T23:59:59.999999", "31.12.1999", False),
        # Некорректные даты
        ("2024-03-11", None, True),  # Без времени
    ],
)
def test_get_date(date_str: str, expected: Optional[str], raises_exception: bool) -> None:
    """Тестовая функция get_date с использованием parametrize."""
    if raises_exception:
        with pytest.raises(ValueError, match="Неверный формат даты"):
            get_date(date_str)
    else:
        assert get_date(date_str) == expected
