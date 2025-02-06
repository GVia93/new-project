from src.widget import get_date, mask_account_card


def main():
    print(get_date("2024-03-11T02:26:18.671407"))

    card_info = "Visa Platinum 1234567890123456"
    card_info_1 = "Счет 12345678901234567890"

    print(mask_account_card(card_info))
    print(mask_account_card(card_info_1))


if __name__ == "__main__":
    main()
