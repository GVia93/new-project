import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/masks.log")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str | None:
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
    card_number = card_number.replace(" ", "").replace("-", "")

    if not card_number or not card_number.isdigit():
        logger.error(f"Не корректные формат: {card_number}")
        return None

    if len(card_number) not in (15, 16, 19):
        logger.error(f"Не корректная длина номера: {len(card_number)}")
        return None

    if len(card_number) == 16:
        masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    elif len(card_number) == 15:
        masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-3:]}"
    elif len(card_number) == 19:
        masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:16]} {card_number[-3:]}"

    logger.info(f"Номер замаскирован: {masked_number}")
    return masked_number


def get_mask_account(account_number: str) -> str | None:
    """
    Маскирует номер банковского счета по заданному шаблону.

    Формат маскирования:
    - Если номер состоит из 20 цифр, возвращается строка вида **XXXX (где XXXX — последние 4 цифры счета).
    - Если данные некорректны (нечисловой ввод, неверная длина), возвращается строка 'Не корректные данные'.

    :param account_number: Строка, содержащая номер банковского счета (может включать пробелы или дефисы).
    :return: Маскированный номер счета или сообщение об ошибке.
    """
    account_number = account_number.replace(" ", "").replace("-", "")

    if not account_number or not account_number.isdigit():
        logger.error(f"Не корректные формат: {account_number}")
        return None

    if len(account_number) == 20:
        masked_number = f"**{account_number[-4:]}"
        logger.info(f"Номер замаскирован: {masked_number}")
        return masked_number
    else:
        logger.error(f"Не корректная длина номера: {len(account_number)}")
        return None
