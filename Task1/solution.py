from math import cos, exp2, isclose, log, sin


# Заданная функция.
# float в Python имеет точность double.
def f(x):
    return exp2(-x) - sin(x)


# Производная заданной функции.
def df(x):
    return -exp2(-x) * log(2) - cos(x)


# Процедура отделения корней.
def segmentation(f, a, b, n):
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
def bisection(f, a, b, abs_tol):
    steps = 0
    while abs(b - a) >= (2 * abs_tol):
        steps += 1
        c = (a + b) / 2

        if f(a) * f(c) <= 0:
            b = c
        else:
            a = c

    root = (a + b) / 2
    delta = abs(b - a) / 2

    return root, delta, steps


# Метод Ньютона приближения корня нелинейного уравнения.
def newton(f, df, x0, abs_tol, max_iter):
    x_curr = x0

    # Метод Ньютона может не сойтись.
    # Используем ограничение на количество итераций.
    for i in range(1, max_iter + 1):
        f_x_curr = f(x_curr)
        df_x_curr = df(x_curr)

        # Метод не работает в случае значения нулю производной.
        if isclose(df_x_curr, 0):
            return None, i

        # Вычисление и проверка приближенного значения корня.
        xn_prev = x_curr
        x_curr = x_curr - f_x_curr / df_x_curr

        if abs(x_curr - xn_prev) < abs_tol:
            return x_curr, i

    return None, max_iter


# Упрощенный метод Ньютона приближения корня нелинейного уравнения.
def modified_newton(f, df, x0, abs_tol, max_iter):
    x_curr = x0

    # Упрощение в единственном вычислении производной.
    df_x0 = df(x0)

    if isclose(df_x0, 0):
        return None, 0

    for i in range(1, max_iter + 1):
        f_x_curr = f(x_curr)

        xn_prev = x_curr
        x_curr = x_curr - f_x_curr / df_x0

        if abs(x_curr - xn_prev) < abs_tol:
            return x_curr, i

    return None, max_iter


# Метод секущих приближения корня нелинейного уравнения.
def secant(f, x0, x1, abs_tol, max_iter):
    x_prev = x0
    x_curr = x1

    # Метод секущих может не сойтись.
    # Используем ограничение на количество итераций.
    for i in range(1, max_iter + 1):
        f_x_prev = f(x_prev)
        f_x_curr = f(x_curr)

        # Метод не работает в случае значения нулю приблежения производной.
        if isclose(x_curr - x_prev, 0):
            return None, i

        df = (f_x_curr - f_x_prev) / (x_curr - x_prev)

        # Вычисление и проверка приближенного значения корня.
        x_prev = x_curr
        x_curr = x_curr - f_x_curr / df

        if abs(x_curr - x_prev) < abs_tol:
            return x_curr, i

    return None, max_iter
