from typing import Tuple

from Function import Function
from Result import Result


class AbstractMethod:
    name = None

    def __init__(self):
        self.log = None
        self.decimal_places = None
        self.epsilon = None
        self.right = None
        self.left = None
        self.equation = None

    def set_values(self, equation: Function, left: float, right: float,
                 epsilon: float, decimal_places: int, log: bool):
        self.log = log
        self.decimal_places = decimal_places
        self.epsilon = epsilon
        self.right = right
        self.left = left
        self.equation = equation

    def solve(self) -> Result:
        pass

    def check(self) -> Tuple[bool, str]:
        return True, ''