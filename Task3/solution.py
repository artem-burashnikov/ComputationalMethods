from collections.abc import Callable
from numpy import exp, log

# Номер варианта
V = 2
# Константа для экспоненты
K = (V % 5) + 1


# Тестовая функция №1
def f1(x: float):
    return log(1.0 + x)


# Первая производная функции №1
def df1(x: float):
    return 1.0 / (1.0 + x)


# Вторая производная функции #1
def d2f1(x: float):
    return - 1.0 / ((1.0 + x) ** 2)


# Тестовая функция №2
def f2(x: float):
    return exp(1.5 * K * x)


# Первая производная функции №2
def df2(x: float):
    return 1.5 * K * f2(x)


# Вторая производная функции #2
def d2f2(x: float):
    return 1.5 * K * df2(x)


# Поиск 1ой производной методом численного дифференцирования с погрешностью O(h^2)
def dfh2(d: Callable[[float], float], index: int, points: list[tuple[float, float]], h: float):
    # Формула зависит от положения точки в таблице
    if index == 0:
        dfh2x = (-3.0 * points[0][1] + 4.0 * points[1][1] - points[2][1]) / (2.0 * h)
    elif index == len(points) - 1:
        dfh2x = (3.0 * points[-1][1] - 4.0 * points[-2][1] + points[-3][1]) / (2.0 * h)
    else:
        dfh2x = (points[index + 1][1] - points[index - 1][1]) / (2.0 * h)
    return dfh2x, abs(d(points[index][0]) - dfh2x)


# Поиск 1ой производной методом численного дифференцирования с погрешностью O(h^4)
def dfh4(d: Callable[[float], float], index: int, points: list[tuple[float, float]], h: float):
    # Формула зависит от положения точки в таблице
    if index == 0:
        dfh4x = (-25 * points[0][1] + 48 * points[1][1] - 36 * points[2][1] + 16 * points[3][1] - 3 * points[4][1]) / (12 * h)
    elif index == 1:
        dfh4x = (-3 * points[0][1] - 10 * points[1][1] + 18 * points[2][1] - 6 * points[3][1] + points[4][1]) / (12 * h)
    elif index == len(points) - 2:
        dfh4x = (3 * points[-1][1] + 10 * points[-2][1] - 18 * points[-3][1] + 6 * points[-4][1] - points[-5][1]) / (12 * h)
    elif index == len(points) - 1:
        dfh4x = (25 * points[-1][1] - 48 * points[-2][1] + 36 * points[-3][1] - 16 * points[-4][1] + 3 * points[-5][1]) / (12 * h)
    else:
        dfh4x = (points[index - 2][1] - 8 * points[index - 1][1] + 8 * points[index + 1][1] - points[index + 2][1]) / (12 * h)
    return dfh4x, abs(d(points[index][0]) - dfh4x)


# Поиск 2ой производной методом численного дифференцирования с погрешностью O(h^2)
def d2fh2(d: Callable[[float], float], index: int, points:list[tuple[float, float]], h: float):
    # Формула зависит от положения точки в таблице
    if index == 0:
        d2fh2x = (2 * points[0][1] - 5 * points[1][1] + 4 * points[2][1] - points[3][1]) / (h ** 2)
    elif index == len(points) - 1:
        d2fh2x = (2 * points[-1][1] - 5 * points[-2][1] + 4 * points[-3][1] - points[-4][1]) / (h ** 2)
    else:
        d2fh2x = (points[index + 1][1] - 2 * points[index][1] + points[index - 1][1]) / (h ** 2)
    return d2fh2x, abs(d(points[index][0]) - d2fh2x)


# Создать узлы
def generate_nodes(x0: float, h: float, node_count: int):
    result = []
    if node_count > 0:
        for i in range(node_count):
            node = x0 + i * h
            result.append(node)
    return result


# Создать точки (x_i, f(x_i))
def generate_points(x_arr: list[float], f: Callable[[float], float]):
    return [(x, f(x)) for x in x_arr]
