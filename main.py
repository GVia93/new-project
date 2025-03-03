from src.processing import filter_by_description, filter_by_state, sort_by_date
from src.utils import load_transactions_csv, load_transactions_excel, load_transactions_json
from src.widget import get_date, mask_account_card


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Ваш выбор: ")

    if choice == "1":
        file_path = "data/operations.json"
        transactions = load_transactions_json(file_path)
        print("Для обработки выбран JSON-файл.")
    elif choice == "2":
        file_path = "data/transactions.csv"
        transactions = load_transactions_csv(file_path)
        print("Для обработки выбран CSV-файл.")
    elif choice == "3":
        file_path = "data/transactions_excel.xlsx"
        transactions = load_transactions_excel(file_path)
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Неверный выбор. Программа завершена.")
        return

    while True:
        state = input(
            "Введите статус, по которому необходимо выполнить фильтрацию."
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: "
        ).upper()
        state.encode("utf-8").decode("utf-8")
        if state in ["EXECUTED", "CANCELED", "PENDING"]:
            break
        print(f"Статус операции '{state}' недоступен.")

    transactions = filter_by_state(transactions, state)
    print(f"Операции отфильтрованы по статусу '{state}'")

    sort_choice = input("Отсортировать операции по дате? Да/Нет: ").lower()
    if sort_choice == "да":
        order = input("Отсортировать по возрастанию или по убыванию? ").lower()
        reverse = order == "по убыванию"
        transactions = sort_by_date(transactions, reverse)

    rub_only = input("Выводить только рублевые транзакции? Да/Нет: ").lower()
    if rub_only == "да":
        transactions = [
            t
            for t in transactions
            if "operationAmount" in t
            and "currency" in t["operationAmount"]
            and t["operationAmount"]["currency"].get("code") == "RUB"
        ]

    search_description = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").lower()
    if search_description == "да":
        search_string = input("Введите строку для поиска в описании: ")
        search_string.encode("utf-8").decode("utf-8")
        transactions = filter_by_description(transactions, search_string)

    print("Распечатываю итоговый список транзакций...")
    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(transactions)}")
        for transaction in transactions:
            date = get_date(transaction.get("date"))
            description = transaction.get("description")

            if "operationAmount" in transaction:
                amount = transaction["operationAmount"].get("amount")
                currency = transaction["operationAmount"].get("currency").get("code")
            else:
                amount = transaction.get("amount")
                currency = transaction.get("currency_code")

            if "from" in transaction:
                from_value = str(transaction.get("from"))
                from_account = mask_account_card(from_value)
            else:
                from_account = None

            to_value = str(transaction.get("to"))
            to_account = mask_account_card(to_value)

            if from_account:
                print(f"{date} {description}\n{from_account} -> {to_account}\nСумма: {amount} {currency}\n")
            else:
                print(f"{date} {description}\nСчет {to_account}\nСумма: {amount} {currency}\n")


if __name__ == "__main__":
    main()
