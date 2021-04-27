import decimal
import math
from typing import Tuple

from Function import Function
from methods.AbstractMethod import AbstractMethod
from methods.HalfDivisionMethod import HalfDivisionMethod
from methods.NewtonsMethod import NewtonsMethod
from methods.SimpleIterationMethod import SimpleIterationMethod

functions = [
    Function(lambda x: -1.8 * (x ** 3) - 2.94 * (x ** 2) + 10.37 * x + 5.38,
             '−1.8x^3 − 2.94x^2 + 10.37x + 5.38'),
    # https://cutt.ly/6zNbCha
    Function(lambda x: (x / 2.0 - 2.0 * (x + 2.39) ** (1.0 / 3.0)),
             'x/2 - 2*(x + 2.39)^(1/3)'),
    # https://cutt.ly/MzNdHH5
    Function(lambda x: (-x / 2 + math.e ** x + 5 * math.sin(x)),
             '-x/2 + e^x + 5*sin(x)')
]

methods = [
    HalfDivisionMethod(),
    NewtonsMethod(),
    SimpleIterationMethod()
]

def choose_function():
    print('Предложенные функции:')
    for i, x in enumerate(functions):
        print(f'{i + 1}. {x}')

    user_input = None

    try:
        user_input = int(input('Выберите функцию (введите одно число): ')) - 1
    except ValueError:
        print("ОШИБКА!!! Введено не число.")
        exit(1)

    if user_input > len(functions):
        print(f'ОШИБКА!!!! Надо было ввести число от 1 до {len(functions) + 1}.'
              f' Теперь заново запускай программу и вводи всё...')
        exit(1)

    print(f'Выбрана функция под номером {user_input + 1}')
    return functions[user_input]


def choose_method():
    print('Вашему вниманию предлагаются следующие методы:')
    for i, x in enumerate(methods):
        print(f'{i + 1}. {x.name}')

    user_input = None

    try:
        user_input = int(input('Выберите метод (введите одно число): ')) - 1
    except ValueError:
        print("ОШИБКА!!! Введено не число.")
        exit(1)

    if user_input > len(functions):
        print(f'ОШИБКА!!!! Надо было ввести число от 1 до {len(functions) + 1}.'
              f' Теперь заново запускай программу и вводи всё...')
        exit(1)

    print(f'Выбран метод под номером {user_input + 1}: {methods[user_input].name}')
    return methods[user_input]


def read_initial_data() -> Tuple[float, float, float, int]:
    while True:
        filename = input("Введите имя файла для загрузки исходных данных и интервала "
                         "или пустую строку, чтобы ввести вручную: ")
        if filename == '':
            left = float(input('Введите левую границу интервала: '))
            right = float(input('Введите правую границу интервала: '))
            epsilon = input('Введите погрешность вычисления: ')
            break
        else:
            try:
                f = open(filename, "r")
                left = float(f.readline())
                right = float(f.readline())
                epsilon = f.readline()
                f.close()
                print('Считано из файла:')
                print(f'Левая граница: {left}, правая: {right}, погрешность: {epsilon}')
                break
            except FileNotFoundError:
                print('(!) Файл для загрузки исходных данных не найден.')

    decimal_places = abs(decimal.Decimal(epsilon).as_tuple().exponent)
    epsilon = float(epsilon)

    return left, right, epsilon, decimal_places
