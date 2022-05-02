from decimal import Decimal
from exceptions import WrongInput


class Calculator:

    def __init__(self):
        self.last_memory: int | Decimal = 0

    def addition(self, first, second) -> int:
        """Addition method"""

        self.last_memory = first + second
        return self.last_memory

    def subtraction(self, first, second) -> int:
        """subtraction method"""

        self.last_memory = first - second
        return self.last_memory

    def multiplication(self, first, second) -> int:
        """multiplication method"""

        self.last_memory = first * second
        return self.last_memory

    def division(self, first, second) -> int:
        """division method"""
        if second == 0:
            raise WrongInput("Input error, can't divide by 0")

        self.last_memory = first / second
        return self.last_memory
