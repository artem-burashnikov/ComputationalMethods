from numpy import array, log, ndarray

# Выбор узлов интерполирования зависит от того, где находится точка x_new.
# Пусть h = (b - a) / n
# 1) Если b - h/2 <= x_new < b, то узлы стоит выбирать в следующем порядке: b, b - h, b - 2h и т.д...
# 2) Если x_k < x_new <= x_k + h/2, то узлы стоит выбирать такие: x_k, x_k - h, x_k + h, x_k - 2h, x_k + 2h и т.д...

class LagrangePolyForm:
    pass

def f(x: ndarray):
    if any(x <= -1):
        print("Недопустимое для логарифма значение x")
        return None
    return log(1 + x)


def generate_nodes(a: float, b: float, node_count: int):
    result = []
    if node_count != 0:
        for i in range(node_count):
            node = a + i * abs(b - a) / node_count
            result.append(node)
    return array(result)


def find_closest_nodes():
    pass


def interpolation_poly():
    pass
