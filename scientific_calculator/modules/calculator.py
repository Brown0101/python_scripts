import math


class Calculator(object):
    """ Our class for assiting in mathematical calculations """

    def __init__(self):
        """ Defining our constructor even though we are not using it yet """
        pass

    def perform_operation(self, operand, value1, value2):
        """ Determines the correct math operation to perform """
        if operand == "1":
            self.add(value1, value2)
        elif operand == "2":
            self.subtract(value1, value2)
        elif operand == "3":
            self.multiply(value1, value2)
        elif operand == "4":
            self.divide(value1, value2)
        elif operand == "5":
            self.modulo(value1, value2)
        elif operand == "6":
            self.raising_to_a_power(value1, value2)
        elif operand == "7":
            self.square_root(value1)
        elif operand == "8":
            self.logarithm(value1)
        elif operand == "9":
            self.sine(value1)
        elif operand == "10":
            self.cosine(value1)
        elif operand == "11":
            self.tangent(value1)

    def add(self, value1, value2):
        result = str(value1 + value2)
        print(f"\nThe result is: {result}\n")

    def subtract(self, value1, value2):
        result = str(value1 - value2)
        print(f"\nThe result is: {result}\n")

    def multiply(self, value1, value2):
        result = str(value1 * value2)
        print(f"\nThe result is: {result}\n")

    def divide(self, value1, value2):
        try:
            result = str(value1 / value2)
            print(f"\nThe result is: {result}\n")
        except ZeroDivisionError as error:
            print("You can not divide by Zero.")

    def modulo(self, value1, value2):
        result = str(value1 % value2)
        print(f"\nThe result is: {result}\n")

    def raising_to_a_power(self, value1, value2):
        result = str(math.pow(value1, value2))
        print(f"\nThe result is: {result}\n")

    def square_root(self, value1):
        result = str(math.sqrt(value1))
        print(f"\nThe result is: {result}\n")

    def logarithm(self, value1):
        result = str(math.log(value1, 2))
        print(f"\nThe result is: {result}\n")

    def sine(self, value1):
        result = str(math.sin((math.radians(value1))))
        print(f"\nThe result is: {result}\n")

    def cosine(self, value1):
        result = str(math.cos((math.radians(value1))))
        print(f"\nThe result is: {result}\n")

    def tangent(self, value1):
        result = str(math.tan((math.radians(value1))))
        print(f"\nThe result is: {result}\n")

    def print_menu(self):
        """ Prints our menu to the user """
        print(
            """
            Choose the math operation:
            -------------------------

            1.  Addition
            2.  Subtraction
            3.  Multiplication
            4.  Division
            5.  Modulo
            6.  Raising to a power
            7.  Square Root
            8.  Logarithm
            9.  Sine
            10. Cosine
            11. Tangent
            """
        )


