from unittest.mock import Mock, patch

from src.external_api import convert_to_rub


def test_convert_to_rub():
    """
    Тест транзакции RUB
    """
    transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "RUB"}}}
    result = convert_to_rub(transaction)
    assert result == 100.00


@patch("requests.get")
def test_convert_to_rub_usd(mock_get):
    """
    Тест транзакции USD
    """
    # Мокаем ответ API
    mock_response = Mock()
    mock_response.json.return_value = {"result": 7500.0}
    mock_response.status_code = 200
    mock_get.return_value = mock_response
    transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}}
    result = convert_to_rub(transaction)
    assert result == 7500.0


@patch("requests.get")
def test_convert_to_rub_eur(mock_get):
    """
    Тест транзакции USD
    """
    # Мокаем ответ API
    mock_response = Mock()
    mock_response.json.return_value = {"result": 90.0}
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    transaction = {"operationAmount": {"amount": "1.00", "currency": {"code": "EUR"}}}
    result = convert_to_rub(transaction)
    assert result == 90.0
