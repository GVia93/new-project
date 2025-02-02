from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """
    Маскирует номер карты или банковского счета в заданном формате.

    Ожидаемый формат входных данных:
    - Для карт: "Название карты 1234567890123456" (например, "Visa Platinum 1234567890123456").
    - Для счетов: "Счет 12345678901234567890".

    Форматы маскирования:
    - Карта (16 цифр): "XXXX XX** **** XXXX"
    - Карта (15 цифр): "XXXX XX** **** XXX"
    - Карта (19 цифр): "XXXX XX** **** XXXX XXX"
    - Счет (20 цифр): "**XXXX" (где XXXX — последние 4 цифры счета)

    Если входные данные не соответствуют ожидаемому формату (например, нет пробела между названием и номером,
    содержат некорректные символы или имеют неподходящую длину), функция возвращает "Не корректные данные".

    :param account_card: Строка с номером карты или счета.
    :return: Замаскированный номер карты/счета или "Не корректные данные" в случае ошибки.
    """
    if ' ' not in account_card:
        return 'Не корректные данные'

    space_index = account_card.rfind(' ') + 1
    number = account_card[space_index:].replace('-', '')

    if not number.isdigit():
        return 'Не корректные данные'

    if len(number) not in (15, 16, 19, 20):
        return 'Не корректные данные'

    if len(number) == 20:
        return account_card[:space_index] + get_mask_account(number)
    else:
        return account_card[:space_index] + get_mask_card_number(number)


def get_date(date: str) -> str:
    """
    Преобразует дату из "YYYY-MM-DDTHH:MM:SS.ssssss" в "DD.MM.YYYY".
    Если формат неверный, выбрасывает ValueError.
    """
    try:
        parts = date.split("T")
        if len(parts) != 2:
            raise ValueError("Неверный формат даты")

        return ".".join(parts[0].split("-")[::-1])
    except Exception:
        raise ValueError("Неверный формат даты")
