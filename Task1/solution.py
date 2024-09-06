import numpy as np

from collections.abc import Callable
from typing import Any


EPSILON = 1e-6


def my_function(x: np.float64) -> Any:
    return np.power(2, -x) - np.sin(x)


def bisection(
    f: Callable[[np.float64], Any], a: np.float64, b: np.float64, eps: np.float64
) -> tuple[np.float64, np.float64]:
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
