import pandas as pd
from solution import f, generate_nodes, p, sort_by_distance_to_x

set_yes = {"yes", "да", "y"}

set_no = {"no", "нет", "n"}


def main():
    print("Задача алгебраического интерполирования. Вариант 2.")
    print("Тестовая функция: log(1+x)")
    print("Тестовый отрезок выбора узлов интерполирования: [0;1]")
    print("Тестовое число узлов: 15")
    print("Тестовая точка x: 0.35")
    print("--------------------------------------------------------------------------")
    node_count = int(input("Введите число значений в таблице (m+1): "))  # m = 15
    a = float(input("Введите левую границу отрезка A: "))  # a = 0
    b = float(input("Введите правую границу отрезка B: "))  # b = 1

    x_arr = generate_nodes(a, b, node_count)

    if any(el <= -1 for el in x_arr):
        print("Недопустимое значение узла для тестовой функции")
        exit(1)

    fx_arr = f(x_arr)
    df = pd.DataFrame({"x": x_arr, "f(x)": fx_arr}).rename_axis("id", axis=1)
    print(df.to_string())
    print("--------------------------------------------------------------------------")

    while True:
        x = float(input("Введите точку интерполирования x: "))  # x = 0.35

        n = node_count

        while n >= node_count:
            n = int(input(f"Введите степень интерполяционного многочлена n <= {node_count - 1}: "))  # n = 7
            if n >= node_count:
                print(f"Введено недопустимое значение: {n}.")

        closest_indexed_nodes = sort_by_distance_to_x(x, x_arr)
        closest_indecies = [i[0] for i in closest_indexed_nodes]
        closest_nodes = [x[1] for x in closest_indexed_nodes]
        closest_values = [fx_arr[i] for i in closest_indecies]

        sliced_indecies = closest_indecies[: (n + 1)]
        sliced_x_arr = closest_nodes[: (n + 1)]
        sliced_fx_arr = [fx_arr[i] for i in sliced_indecies]

        df = pd.DataFrame({"id": sliced_indecies, "x": sliced_x_arr, "f(x)": sliced_fx_arr})
        print(df.to_string(index=False))
        print("--------------------------------------------------------------------------")

        pnx = p(n, x, closest_nodes, closest_values)
        fx = f(x)
        abs_tol = abs(fx - pnx)
        print(f"Точка x: {x}")
        print(f"Значение многочлена Лагранжа Pn(x): {pnx}")
        print(f"Значение функции f(x): {fx}")
        print(f"Абсолютная фактическая погрешность: {abs_tol}")
        print("--------------------------------------------------------------------------")

        prompt = input("Завершить выполнение программы? [y/n]: ")

        if prompt.strip().lower() in set_yes:
            break

    return 0


if __name__ == "__main__":
    if main() == 0:
        print("Программа успешно завершена.")
