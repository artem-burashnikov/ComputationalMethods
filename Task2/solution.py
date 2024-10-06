from numpy import array, log


# Тестовая функция
def f(x):
    return log(1 + x)


# Генерирует попарно различные узлы интерполирования в количестве node_count
def generate_nodes(a: float, b: float, node_count: int):
    result = []
    if node_count > 0:
        for i in range(node_count):
            node = a + i * abs(b - a) / node_count
            result.append(node)
    return array(result)


# Сортирует список узлов по увеличению расстояния от точки x
def sort_by_distance_to_x(x, x_arr):
    result = [(i, x_arr[i]) for i in range(len(x_arr))]
    return sorted(result, key=lambda xs: abs(xs[1] - x))


# Вычисляет значения интерполяционного многочлена в форме Лагранжа в точке x
def p(n, x, x_arr, fx_arr):
    px = 0
    for k in range(n + 1):
        lmi = 1
        for i in range(n + 1):
            if i != k:
                lmi *= (x - x_arr[i]) / (x_arr[k] - x_arr[i])
        px += fx_arr[k] * lmi
    return px
