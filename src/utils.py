import json


def load_transactions(file_path: str) -> list:
    """
    Загружает данные о финансовых транзакциях из JSON-файла.

    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            transactions = json.load(file)
            if not isinstance(transactions, list):
                raise ValueError
    except (FileNotFoundError, ValueError, json.JSONDecodeError) as e:
        print(f"Ошибка загрузки файла: {e}")
        return []

    return transactions
