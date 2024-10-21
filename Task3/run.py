from solution import dfh2
from tabulate import tabulate
from solution import (
    d2fh2,
    dfh2,
    dfh4,
    f1,
    f2,
    df1,
    df2,
    d2f1,
    d2f2,
    generate_nodes,
    generate_points,
)


# Список функций, их имен, их первой и второй производных
functions = [f1, f2]
function_names = ["log(1+x)", "exp(4.5x)"]
derivatives1 = [df1, df2]
derivatives2 = [d2f1, d2f2]


# Позволяет пользователю выбрать функцию
def choose_function():
    print("Выберите функцию, для которой будет решаться задача.")
    print("Номера функций:")
    print("0: log(1+x)" + "\n" + "1: exp(4.5x)")
    return int(input("Введите номер функции: "))


# Позволяет пользователю задать начальный узел и шаг
def choose_points(func_id):
    while (
        node_count := int(input("Введите количество значений в таблице (m+1) >= 5: "))
    ) < 5:
        print(f"Введено число значений {node_count} < 5")

    x0 = float(input("Введите начальное значение x0: "))

    while (h := float(input("Введите шаг h > 0: "))) <= 0:
        print(f"Введен некорректный шаг: {h}")

    return generate_points(generate_nodes(x0, h, node_count), functions[func_id]), h


# Выводит узлы (x_i, f(x_i))
def print_points(points: list[tuple[float, float]], func_id, h):
    print(f"Таблица значений {function_names[func_id]} в заданных точках c шагом {h}")
    print(
        tabulate(
            [(i, p[0], p[1]) for i, p in enumerate(points, start=1)],
            tablefmt="fancy_grid",
            # floatfmt=".4f",
            headers=["#", "x", "f(x)"],
        )
    )


# Выводит таблицу с пограшностями вычисления производной численными методами
def print_table(
    points: list[tuple[float, float]],
    h: float,
    func_id: int,
):
    df = derivatives1[func_id]
    d2f = derivatives2[func_id]
    table = []
    for i, _ in enumerate(points):
        fprimexh2, errh2 = dfh2(df, i, points, h)
        fprimexh4, errh4 = dfh4(df, i, points, h)
        fprimeprimexh2, errerrh2 = d2fh2(d2f, i, points, h)
        table.append(
            (
                i + 1,
                points[i][0],
                points[i][1],
                fprimexh2,
                errh2,
                fprimexh4,
                errh4,
                fprimeprimexh2,
                errerrh2,
            )
        )
    print(f"Вычисление производных методами численного дифференцирования для функции {function_names[func_id]}")
    print(
        tabulate(
            table,
            tablefmt="fancy_grid",
            # floatfmt=".4f",
            headers=[
                "#",
                "x",
                "f(x)",
                "f'(x)+O(h^2)",
                "O(h^2)",
                "f'(x)+O(h^4)",
                "O(h^4)",
                "f''(x)+O(h^2)",
                "O(h^2)",
            ],
        )
    )


def main():
    print("Методы численного дифференцирования. Вариант 2.")
    func_id = choose_function()
    print("--------------------------------------------------------------------------")
    points, h = choose_points(func_id)
    print("--------------------------------------------------------------------------")
    print_points(points, func_id, h)
    print("--------------------------------------------------------------------------")
    print_table(points, h, func_id)
    print("--------------------------------------------------------------------------")

    while prompt := input(
        "Выберите шаг\n"
        "0: Выбрать другую функцию\n"
        "1: Ввести новые значения параметров таблицы\n"
        "2: Перейти к уточнению по Рунге\n"
        "3: Выйти\n"
        "Ваш выбор: "
    ):
        match int(prompt):
            case 0:
                # Выбрать функцию, точку и шаг
                func_id = choose_function()
                print(
                    "--------------------------------------------------------------------------"
                )
                points, h = choose_points(func_id)
                print_points(points, func_id, h)
                print(
                    "--------------------------------------------------------------------------"
                )
                print_table(points, h, func_id)
            case 1:
                # Выбрать только точку и шаг, функцию не менять
                points, h = choose_points(func_id)
                print_points(points, func_id, h)
                print(
                    "--------------------------------------------------------------------------"
                )
                print_table(points, h, func_id)
            case 2:
                # Выбрать функцию, точку и шаг, узел для уточнения.
                func_id = choose_function()
                print(
                    "--------------------------------------------------------------------------"
                )
                points1, h1 = choose_points(func_id)
                print_points(points1, func_id, h1)
                print(
                    "--------------------------------------------------------------------------"
                )
                
                while (j := int(input("Введите номер узла: ")) - 1) > len(points1) or j < 0:
                    print(f"Введено некорректное значение индекса {j}. Введите значение от 0 до {len(points1) - 1}")

                # Вычислить уточнение
                points2 = generate_points(generate_nodes(points1[0][0], h1 / 2,  len(points1) * 2 - 1), functions[func_id])

                jh1d1, err_jh1d1 = dfh2(derivatives1[func_id], j * 2, points2, h1 / 2)
                jh2d1, err_jh2d1 = dfh2(derivatives1[func_id], j, points1, h1)
                J1 = (4 * jh1d1 - jh2d1) / 3
                derivative1 = derivatives1[func_id](points2[j * 2][0])
                err_1 = abs(derivative1 - J1)

                table1 = (points2[j * 2][0], points2[j*2][1], jh2d1, err_jh2d1, jh1d1, err_jh1d1, J1, err_1),
                header1 = (
                    "x",
                    "f(x)",
                    "J(h)",
                    "|f'(x) - J(h)|",
                    "J(h/2)",
                    "|f'(x) - J(h/2)",
                    "J`",
                    "|f'(x) - J`",
                )
                print(f"Уточненные значения первой производной")
                print(tabulate(table1, headers=header1, tablefmt="fancy_grid"))

                jh1d2, err_jh1d2 = d2fh2(derivatives2[func_id], j * 2, points2, h1 / 2)
                jh2d2, err_jh2d2 = d2fh2(derivatives2[func_id], j, points1, h1)
                J2 = (4 * jh1d2 - jh2d2) / 3
                derivative2 = derivatives2[func_id](points2[j * 2][0])
                err_2 = abs(derivative2 - J2)

                table2 = (points2[j * 2][0], points2[j*2][1], jh2d2, err_jh2d2, jh1d2, err_jh1d2, J2, err_2),
                header2 = (
                    "x",
                    "f(x)",
                    "J(h)",
                    "|f''(x) - J(h)|",
                    "J(h/2)",
                    "|f''(x) - J(h/2)",
                    "J`",
                    "|f''(x) - J`",
                )
                print(f"Уточненные значения второй производной")
                print(tabulate(table2, headers=header2, tablefmt="fancy_grid"))

            case _:
                return 0


if __name__ == "__main__":
    main()
