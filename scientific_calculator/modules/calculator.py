import math


class Calculator(object):
    """ Our class for assiting in mathematical calculations """

    def __init__(self):
        """ Defining our constructor even though we are not using it yet """
        pass


    def perform_operation(self, operand, value1, value2):
        print("Operand is: " + operand)
        if operand == "1":
            self.add(value1, value2)
        elif operand == "2":
            pass
        elif operand == "3":
            pass
        elif operand == "4":
            pass
        elif operand == "5":
            pass
        elif operand == "6":
            pass
        elif operand == "7":
            pass
        elif operand == "8":
            pass
        elif operand == "9":
            pass
        elif operand == "10":
            pass


    def add(self, value1, value2):
        result = str(value1 + value2)
        print(f"\nThe result is: {result}\n")


    def subtract(self, value1, value2):
        pass


    def multiply(self, value1, value2):
        pass


    def divide(self, value1, value2):
        pass


    def Modulo(self, value1, value2):
        pass


    def raising_to_a_power(self, value1, value2):
        pass


    def logarithm(self, value1, value2):
        pass


    def sine(self, value1, value2):
        pass


    def cosine(self, value1, value2):
        pass


    def tangent(self, value1, value2):
        pass


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
            7.  Logarithm
            8.  Sine
            9.  Cosine
            10. Tangent
            """
        )


