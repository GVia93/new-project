def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты по заданному шаблону.

    Формат маскирования:
    - 16-значный номер: XXXX XX** **** XXXX
    - 15-значный номер: XXXX XX** **** XXX
    - 19-значный номер: XXXX XX** **** XXXX XXX

    Если переданы некорректные данные (например, нечисловой ввод или длина, отличная от 15, 16 или 19),
    функция возвращает строку 'Не корректные данные'.

    :param card_number: Строка, содержащая номер карты (может включать пробелы или дефисы).
    :return: Маскированный номер карты или сообщение об ошибке.
    """
    card_number = card_number.replace(' ', '').replace('-', '')

    if not card_number or not card_number.isdigit():
        return 'Не корректные данные'

    if len(card_number) not in (15, 16, 19):
        return 'Не корректные данные'

    if len(card_number) == 16:
        masked_number = f'{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}'
    elif len(card_number) == 15:
        masked_number = f'{card_number[:4]} {card_number[4:6]}** **** {card_number[-3:]}'
    elif len(card_number) == 19:
        masked_number = f'{card_number[:4]} {card_number[4:6]}** **** {card_number[12:16]} {card_number[-3:]}'

    return masked_number


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета по заданному шаблону.

    Формат маскирования:
    - Если номер состоит из 20 цифр, возвращается строка вида **XXXX (где XXXX — последние 4 цифры счета).
    - Если данные некорректны (нечисловой ввод, неверная длина), возвращается строка 'Не корректные данные'.

    :param account_number: Строка, содержащая номер банковского счета (может включать пробелы или дефисы).
    :return: Маскированный номер счета или сообщение об ошибке.
    """
    account_number = account_number.replace(' ', '').replace('-', '')

    if not account_number or not account_number.isdigit():
        return 'Не корректные данные'

    if len(account_number) == 20:
        masked_number = f"**{account_number[-4:]}"
        return masked_number
    else:
        return 'Не корректные данные'
