from modules.calculator import Calculator


def number_validator(count):
    """ Validates our users input for value 1 and 2 """
    number = ""

    while True:
        if count == 1:
            number = input("Enter the first value: ")
        else:
            number = input("Enter the second value: ")

        try:
            float(number)
            break
        except ValueError as error:
            print("ERROR: You must enter in an integer.")

    return float(number)


def main():
    """ Starts our main method """
    VALID_CHOICE = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
    calculator = Calculator()
    cont = ""
    value1 = ""
    value2 = ""

    while True:
        count = 1
        calculator.print_menu()

        operand = input("Your option from the menu (1 - 10): ")

        if operand in VALID_CHOICE:
            value1 = number_validator(count)
            count += 1
            value2 = number_validator(count)

            # Perform our operation
            calculator.perform_operation(operand, value1, value2)
        else:
            print("\n=================== ERROR =========================")
            print(f"You chose {operand}. This is NOT a valid option.")
            print("===================================================")
            continue

        while True:
            if cont.upper() != "Y" or cont.upper() != "N":
                cont = input("Do you want to perform another calculation (Y/N): ")
            else:
                break

        if cont.upper() != "N":
            break


if __name__ == "__main__":
    main()
