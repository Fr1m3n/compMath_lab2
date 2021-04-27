from Function import Function
from InputUtils import choose_function, choose_method, read_initial_data
from methods.AbstractMethod import AbstractMethod


def f(x):
    return -1.8 * (x ** 3) - 2.94 * (x ** 2) + 10.37 * x + 5.38
# roots ranges: [-.6; -.4], [-3.2; -3], [1.9; 2.1]


if __name__ == '__main__':
    f = choose_function()
    f.draw(-4.0, 3.0)
    method = choose_method()
    left, right, epsilon, decimal_places = read_initial_data()
    method.set_values(f, left, right, epsilon, decimal_places, True)
    check_result, error_text = method.check()
    if check_result:
        print(method.solve())
    else:
        print(error_text)
