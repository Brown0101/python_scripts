from modules.calculator import Calculator

# Global variable shared by all methods
valid_choice = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11")

def number_validator(operand, count):
    """ Validates our users input for value 1 and 2 """
    number = ""

    while True:
        if count == 1 and operand not in valid_choice[5:]:
            number = input("Enter the first value: ")
        elif count == 2 and operand not in valid_choice[5:]:
            number = input("Enter the second value: ")
        elif count == 1 and operand == "6":
            number = input("Enter the base: ")
        elif count == 2 and operand == "6":
            number = input("Enter in the power: ")
        elif operand == "7":
            number = input("Enter value for extracting the square root: ")
        elif operand == "8":
            number = input("Enter value for calculating the logarithm to base: ")
        elif operand == "9":
            number = input("Enter value (degrees) for calculating the sine: ")
        elif operand == "10":
            number = input("Enter value (degrees) for calculating the cosine: ")
        elif operand == "11":
            print("I am here")
            number = input("Enter value (degrees) for calculating the tangent: ")

        try:
            float(number)
            break
        except ValueError as error:
            print("ERROR: You must enter in an integer.")

    return float(number)


def main():
    """ Starts our main method """
    calculator = Calculator()

    while True:
        count = 1
        cont = ""
        value1 = None
        value2 = None
        calculator.print_menu()

        operand = input("Your option from the menu (1 - 10): ")

        if operand in valid_choice and operand not in valid_choice[6:]:
            value1 = number_validator(operand, count)
            count += 1
            value2 = number_validator(operand, count)
        elif operand in valid_choice and operand == "7":
            value1 = number_validator(operand, count)
        elif operand in valid_choice and operand == "8":
            value1 = number_validator(operand, count)
        elif operand in valid_choice and operand == "9":
            value1 = number_validator(operand, count)
        elif operand in valid_choice and operand == "10":
            print("I am here")
            value1 = number_validator(operand, count)
        elif operand in valid_choice and operand == "11":
            value1 = number_validator(operand, count)
        else:
            print("\n=================== ERROR =========================")
            print(f"You chose {operand}. This is NOT a valid option.")
            print("===================================================")
            continue

        # Perform our operation
        calculator.perform_operation(operand, value1, value2)

        # Ask if user wants to continue
        while True:
            if cont.upper() != "Y" and cont.upper() != "N":
                cont = input("Do you want to perform another calculation (Y/N): ")
            else:
                break

        # Check if program should exit.
        if cont.upper() == "N":
            print("Exiting program...")
            break


# Start the program. Checks if this is the .py being executed.
if __name__ == "__main__":
    main()
