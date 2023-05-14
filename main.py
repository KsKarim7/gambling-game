MAX_LINES = 3


def deposit():
    while True:
        amount = input("What would you like to deposit? $ ")
        if (amount.isdigit()):
            amount = int(amount)
            if (amount > 0):
                break
            else:
                print("\nAmount must be greater than zero!")
        else:
            print("\nPlease enter a valid number!\n")
    return amount


def get_number_of_lines():
    while True:
        lines = input(
            f"Enter the number of lines to bet on (1-{MAX_LINES})? ")
        if (lines.isdigit()):
            lines = int(lines)
            if (1 <= lines <= MAX_LINES):
                break
            else:
                print("\nEnter a valid number of lines.!")
        else:
            print("\nPlease enter a valid number!\n")
    return lines


def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)


main()
