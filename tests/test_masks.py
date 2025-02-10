import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected_output",
    [
        # Корректные номера карт
        ("1234567890123456", "1234 56** **** 3456"),
        ("1234 5678 9012 3456", "1234 56** **** 3456"),
        ("1234-5678-9012-3456", "1234 56** **** 3456"),
        ("123456789012345", "1234 56** **** 345"),
        ("1234567890123456789", "1234 56** **** 3456 789"),
        # Некорректные данные
        ("", "Не корректные данные"),
        ("   ", "Не корректные данные"),
        ("abcde", "Не корректные данные"),
        ("1234!5678@9012#3", "Не корректные данные"),
        ("1234 5678 9012 3456 7890", "Не корректные данные"),
        ("1234 5678 9012", "Не корректные данные"),
    ],
)
def test_get_mask_card_number(card_number: str, expected_output: str) -> None:
    """Тестовая функция get_mask_card_number с использованием parametrize."""
    assert get_mask_card_number(card_number) == expected_output


@pytest.mark.parametrize(
    "account_number, expected_output",
    [
        # Корректные номера карт
        ("12345678901234567890", "**7890"),
        ("1234 5678 9012 3456 7890", "**7890"),
        ("1234-5678-9012-3456-7890", "**7890"),
        # Некорректные данные
        ("", "Не корректные данные"),
        ("   ", "Не корректные данные"),
        ("abcde", "Не корректные данные"),
        ("1234!5678@9012#37890", "Не корректные данные"),
        ("1234 5678 9012 3456 78901", "Не корректные данные"),
        ("1234 5678 9012", "Не корректные данные"),
    ],
)
def test_get_mask_account(account_number: str, expected_output: str) -> None:
    """Тестовая функция get_mask_account с использованием parametrize."""
    assert get_mask_account(account_number) == expected_output
