from collections.abc import Callable
from Task1.constants import MyFloat


def bisection(
    f: Callable[[MyFloat], MyFloat], a: MyFloat, b: MyFloat, eps: MyFloat
) -> tuple[MyFloat, MyFloat]:
    while (b - a) > (2 * eps):
        c = (a + b) / 2
        if (f(a) * f(c)) <= 0:
            b = c
        else:
            a = c

    root = (a + b) / 2
    delta = (b - a) / 2

    return root, delta


def newton() -> None:
    pass


def modified_newton() -> None:
    pass


def secant() -> None:
    pass
