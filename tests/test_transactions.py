from unittest.mock import mock_open, patch

import pandas as pd
import pytest

from src.transactions import transactions_csv, transactions_excel


@pytest.fixture
def valid_transactions_csv():
    # Данные, которые будут возвращаться при вызове open
    csv_data = (
        "date;amount;description\n" "2023-10-01;100;Salary\n" "2023-10-02;-20;Groceries\n" "2023-10-03;-50;Utilities\n"
    )

    # Ожидаемый результат
    expected = [
        {"date": "2023-10-01", "amount": "100", "description": "Salary"},
        {"date": "2023-10-02", "amount": "-20", "description": "Groceries"},
        {"date": "2023-10-03", "amount": "-50", "description": "Utilities"},
    ]

    return csv_data, expected


@patch("builtins.open", new_callable=mock_open)
def test_transactions_csv(mock_file, valid_transactions_csv):
    """
    Тестирует успешную загрузку транзакций из CSV-файла.
    Ожидается, что функция вернет список транзакций.
    """
    csv_data, expected = valid_transactions_csv
    mock_file = mock_open(read_data=csv_data)
    with patch("builtins.open", mock_file):
        result = transactions_csv("dummy_filename.csv")

    assert result == expected


@patch("builtins.open", side_effect=FileNotFoundError)
def test_transactions_csv_file_not_found(mock_open):
    """
    Тестирует обработку случая, когда CSV-файл не существует.
    Ожидается, что функция вернет пустой список, если файл не найден.
    """
    result = transactions_csv("dummy_filename.csv")
    assert result == []


@pytest.fixture
def valid_transactions_excel():
    # Данные, которые будут возвращаться при вызове pd.read_excel
    excel_data = [
        {"date": "2023-10-01", "amount": 100, "description": "Salary"},
        {"date": "2023-10-02", "amount": -20, "description": "Groceries"},
        {"date": "2023-10-03", "amount": -50, "description": "Utilities"},
    ]

    # Ожидаемый результат
    expected = [
        {"date": "2023-10-01", "amount": 100, "description": "Salary"},
        {"date": "2023-10-02", "amount": -20, "description": "Groceries"},
        {"date": "2023-10-03", "amount": -50, "description": "Utilities"},
    ]

    return excel_data, expected


@patch("pandas.read_excel")
def test_transactions_excel(mock_read_excel, valid_transactions_excel):
    """
    Тестирует успешную загрузку транзакций из Excel-файла.
    Ожидается, что функция вернет список транзакций.
    """
    excel_data, expected = valid_transactions_excel
    mock_read_excel.return_value = pd.DataFrame(excel_data)
    result = transactions_excel("dummy_filename.xlsx")
    assert result == expected
    mock_read_excel.assert_called_once_with("dummy_filename.xlsx")


@patch('pandas.read_excel', side_effect=FileNotFoundError)
def test_transactions_excel_file_not_found(mock_read_excel):
    """
    Тестирует обработку случая, когда Excel-файл не существует.
    Ожидается, что функция вернет пустой список, если файл не найден.
    """
    result = transactions_excel("dummy_filename.excel")
    assert result == []
