from Result import Result
from methods.AbstractMethod import AbstractMethod
import math
from scipy.misc.common import derivative

class NewtonsMethod(AbstractMethod):

    def __init__(self):
        super().__init__()
        self.name = 'Метод Ньютона'
        self.phi = None

    def solve(self):
        iteration = 0
        x0 = self.right
        f = self.equation.f
        h = f(x0) / derivative(f, x0)
        x = x0 - h
        crutch = "f\'"
        print(f'{"Xk":^10} {"f(Xk)":^10} {(crutch + "(Xk)"):^10} {"Xk + 1":^10} {"|Xk - Xk + 1|":^10}')
        while True:
            iteration += 1
            prev_x = x
            x = prev_x - f(prev_x) / derivative(f, prev_x)
            print(f'{prev_x:^10.3f} {f(prev_x):^10.3f} {derivative(f, prev_x):^10.3f} {x:^10.3f} {abs(prev_x - x):^10.3f}')
            if abs(prev_x - x) <= self.epsilon:
                break

        return Result(x, f(x), iteration, self.decimal_places)
