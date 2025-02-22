import os

import requests
from dotenv import load_dotenv


def convert_to_rub(transaction: dict) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    Если транзакция уже в рублях (RUB), возвращается исходная сумма.
    Если транзакция в USD или EUR, происходит конвертация в рубли через внешний API.
    """
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])
    else:
        # Параметры для обращения к API
        amount = float(transaction["operationAmount"]["amount"])
        currency = transaction["operationAmount"]["currency"]["code"]

        # Загрузка переменных из .env-файла
        load_dotenv(".env")

        # Получение значения переменной TOKEN из .env-файла
        API_KEY = os.getenv("API_KEY")

        url = "https://api.apilayer.com/exchangerates_data/convert"

        payload = {"amount": amount, "from": currency, "to": "RUB"}
        headers = {"apikey": API_KEY}

        response = requests.get(url, headers=headers, params=payload)

        result = response.json()
        return float(result["result"])
