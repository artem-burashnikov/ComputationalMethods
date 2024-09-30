import pandas as pd
from solution import f, generate_nodes

set_yes = {"yes", "да", "y"}

set_no = {"no", "нет", "n"}


def main():
    print("Задача алгебраического интерполирования. Вариант 2.")
    print("--------------------------------------------------------------------------")
    node_count = int(input("Введите число значений в таблице (m+1): "))  # m = 15
    a = float(input("Введите левую границу отрезка A: "))  # a = 0
    b = float(input("Введите правую границу отрезка B: "))  # b = 1

    x_arr = generate_nodes(a, b, node_count)
    fx_arr = f(x_arr)
    df = pd.DataFrame({"x": x_arr, "f(x)": fx_arr}).rename_axis("id", axis=1)
    print("--------------------------------------------------------------------------")
    print(df.to_string())

    while True:
        x = float(input("Введите точку интерполирования x: "))  # x = 0.35

        n = node_count

        while n >= node_count:
            n = int(
                input(
                    f"Введите степень интерполяционного многочлена n <= {node_count - 1}: "
                )
            )  # n = 7
            if n >= node_count:
                print(f"Введено недопустимое значение: {n}.")

        # TODO closest_nodes = find_closest_nodes(x, x_arr, f, n)

        # TODO p(x) = interpolation_poly(x, closest_nodes, f)

        # TODO abs_tol = abs(f(x) - p(x))

        prompt = input("Завершить выполнение программы? [y/n]: ")

        if prompt.strip().lower() in set_yes:
            break

    return 0


if __name__ == "__main__":
    if main() == 0:
        print("Программа успешно завершена.")
