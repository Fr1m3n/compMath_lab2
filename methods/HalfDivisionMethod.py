from Function import Function
from Result import Result
from methods.AbstractMethod import AbstractMethod


class HalfDivisionMethod(AbstractMethod):

    def __init__(self):
        super().__init__()
        self.name = 'Метод половинного деления'

    def solve(self) -> Result:
        f = self.equation.f
        a = self.left
        b = self.right
        epsilon = self.epsilon
        iteration = 0
        while True:
            iteration += 1
            fa = f(a)
            fb = f(b)
            x = (a + b) / 2
            fx = f(x)
            if self.log:
                print(f'{iteration}: a = {a:.3f}, b = {b:.3f}, x = {x:.3f}, '
                      f'f(a) = {fa:.3f}, f(b) = {fb:.3f}, f(x)={fx:.3f}, |a-b| = {abs(a - b):.3f}')
            if abs(a - b) <= epsilon or abs(fx) <= epsilon:
                break
            if fa * fx < 0:
                b = x
            else:
                a = x
        return Result(x, fx, iteration, self.decimal_places)

    def check(self):
        root_exists = self.equation.root_exists(self.left, self.right)
        return root_exists, 'Отсутствует корень на заданном промежутке' if not root_exists else ''
