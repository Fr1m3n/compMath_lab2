from typing import Callable
import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import derivative

dx = 0.00001


class Function:

    def __init__(self, function: Callable, text: str):
        self.text = text
        self.f = function

    def draw(self, left: float, right: float):
        x = np.linspace(left, right)
        func = np.vectorize(self.f)(x)

        plt.title = 'График заданной функции'
        plt.grid(True, which='both')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.axhline(y=0, color='gray', label='y = 0')
        plt.plot(x, func, 'blue', label=self.text)
        plt.legend(loc='upper left')
        plt.savefig('graph.png')
        plt.show()

    def __str__(self):
        return self.text

    def root_exists(self, left: float, right: float):
        return (self.f(left) * self.f(right) < 0) \
               and (derivative(self.f, left, dx) * derivative(self.f, left, dx) > 0)
