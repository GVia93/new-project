from unittest.mock import mock_open, patch

from src.utils import load_transactions


@patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1, "amount": 100}]')
def test_load_transactions_success(mock_file):
    """
    Тестирует успешную загрузку транзакций из JSON-файла.
    Ожидается, что функция вернет список транзакций, если файл существует и содержит валидный JSON-список.
    """
    result = load_transactions("dummy_path.json")
    assert result == [{"id": 1, "amount": 100}]


@patch("builtins.open", side_effect=FileNotFoundError)
def test_load_transactions_file_not_found(mock_file):
    """
    Тестирует обработку случая, когда файл не существует.
    Ожидается, что функция вернет пустой список, если файл не найден.
    """
    result = load_transactions("nonexistent_file.json")
    assert result == []


@patch("builtins.open", new_callable=mock_open, read_data="invalid json")
def test_load_transactions_invalid_json(mock_file):
    """
    Тестирует обработку случая, когда JSON в файле некорректен.
    Ожидается, что функция вернет пустой список, если JSON не может быть декодирован.
    """
    result = load_transactions("invalid.json")
    assert result == []


@patch("builtins.open", new_callable=mock_open, read_data='{"id": 1, "amount": 100}')
def test_load_transactions_not_a_list(mock_file):
    """
    Тестирует обработку случая, когда JSON в файле не является списком.
    Ожидается, что функция вернет пустой список, если данные не являются списком.
    """
    result = load_transactions("not_a_list.json")
    assert result == []
