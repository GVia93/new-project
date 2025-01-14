from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_info: Union[str]) -> str:
    """
    Принимает аргумент типа Visa Platinum 1234567890123456 или Счет 12345678901234567890.
    Возвращает строку с замаскированным номером.
    """
    space_index = card_info.rfind(" ") + 1
    number = card_info[space_index:]
    if number.isdigit():
        if len(number) == 16:
            return card_info[:space_index] + get_mask_card_number(number)
        elif len(number) == 20:
            return card_info[:space_index] + get_mask_account(number)
    else:
        return "Не корректные данные"
