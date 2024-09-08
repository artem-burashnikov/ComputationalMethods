from collections.abc import Callable
from math import cos, exp2, log, sin


# Заданная функция.
def f(x: float) -> float:
    return exp2(-x) - sin(x)


# Производная заданной функции.
def df(x: float) -> float:
    return -exp2(-x) * log(2) - cos(x)


# Процедура отделения корней.
def segmentation(
    f: Callable[[float], float], a: float, b: float, n: int
) -> list[tuple[float, float]]:
    # Шаг разбиения.
    h = (b - a) / n

    # Отрезки, содержащие корни нечетной кратности.
    segments = []

    # Сдвигаемся на h, пока не вышли за пределы исходного отрезка.
    # Сохраняем отрезки, содержащие корни нечетной кратности.
    x1 = a
    x2 = x1 + h
    y1 = f(x1)

    while x2 <= b:
        y2 = f(x2)

        if y1 * y2 <= 0:
            segments.append((x1, x2))

        x1 = x2
        x2 = x1 + h
        y1 = y2

    return segments


# Алгоритм половинного деления
def bisection(
    f: Callable[[float], float], a: float, b: float, eps: float
) -> tuple[float, float]:
    while abs(b - a) >= (2 * eps):
        c = (a + b) / 2

        if (f(a) * f(c)) <= 0:
            b = c
        else:
            a = c

    root = (a + b) / 2
    delta = abs(b - a) / 2

    return root, delta


# Метод Ньютона приближения корня нелинейного уравнения.
def newton(
    f: Callable[[float], float],
    df: Callable[[float], float],
    x0: float,
    eps: float,
    max_iter: int,
) -> tuple[int, float | None]:
    xn = x0

    # Метод Ньютона может не сойтись.
    # Используем ограничение на количество итераций.
    for i in range(max_iter):
        f_xn = f(xn)
        df_xn = df(xn)

        # Метод не работает в случае значения нулю производной.
        if df_xn == 0:
            return i, None

        # Вычисление и проверка приближенного значения корня.
        xn_prev = xn
        xn = xn - f_xn / df_xn

        if abs(xn - xn_prev) < eps:
            return i, xn

    return max_iter, None


# Упрощенный метод Ньютона приближения корня нелинейного уравнения.
def modified_newton(
    f: Callable[[float], float],
    df: Callable[[float], float],
    x0: float,
    eps: float,
    max_iter: int,
) -> tuple[int, float | None]:
    xn = x0

    # Упрощение в единственном вычислении производной.
    df_x0 = df(x0)

    if df_x0 == 0:
        return 0, None

    for i in range(max_iter):
        f_xn = f(xn)

        xn_prev = xn
        xn = xn - f_xn / df_x0

        if abs(xn - xn_prev) < eps:
            return i, xn

    return max_iter, None
