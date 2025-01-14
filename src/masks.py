from typing import Union


def get_mask_card_number(card_number: Union[str]) -> str:
    """Функция принимает на вход номер карты в виде числа и
    возвращает маску номера по правилу
    XXXX XX** **** XXXX"""
    card_number_blocks = [card_number[:4], card_number[4:8], card_number[8:12], card_number[12:16]]
    return f"{card_number_blocks[0]} {card_number_blocks[1][:2]}** **** {card_number_blocks[3]}"


def get_mask_account(account_number: Union[str]) -> str:
    """Функция принимает на вход номер счета в виде числа и
    возвращает маску номера по правилу **XXXX"""
    return f"**{account_number[-4:]}"
