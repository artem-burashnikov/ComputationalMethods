from solution import f, df, segmentation, bisection, newton, modified_newton, secant


set_yes = {"yes", "да", "y"}

set_no = {"no", "нет", "n"}


def printer(segment, abs_tol):
    print("--------------------------------------------------------------------------")

    print(f"Отрезок: [{segment[0]}; {segment[1]}]")

    root, delta, steps = bisection(f, segment[0], segment[1], abs_tol)
    print(
        "Метод бисекции: \n"
        f"    С точностью {abs_tol} был найден корень: {root}. \n"
        f"    Длина последнего отрезка приближения: {delta} \n"
        f"    Количество шагов для достижения заданного приближения корня: {steps}. \n"
        f"    Абсолютная величина невязки: {abs(f(root))}.\n"
    )

    root, steps = newton(f, df, (segment[0] + segment[1]) / 2, abs_tol, 1000)
    print(
        "Метод Ньютона: \n"
        f"    С точностью {abs_tol} был найден корень: {root}. \n"
        f"    Количество шагов для достижения заданного приближения корня: {steps}.\n"
        f"    Абсолютная величина невязки: {abs(f(root))}.\n"
    )

    root, steps = modified_newton(f, df, (segment[0] + segment[1]) / 2, abs_tol, 1000)
    print(
        "Упрощенный метод Ньютона: \n"
        f"    С точностью {abs_tol} был найден корень: {root}. \n"
        f"    Количество шагов для достижения заданного приближения корня: {steps}.\n"
        f"    Абсолютная величина невязки: {abs(f(root))}.\n"
    )

    root, steps = secant(f, (segment[0] + segment[1]) / 2, segment[1], abs_tol, 1000)
    print(
        f"Метод секущих: \n"
        f"    С точностью {abs_tol} был найден корень: {root}. \n"
        f"    Количество шагов для достижения заданного приближения корня: {steps}.\n"
        f"    Абсолютная величина невязки: {abs(f(root))}.\n"
    )


def main():
    print("Численные методы решения нелинейных уравнений")
    print("Исходные параметры тестовой задачи (вариант 2)")
    print("--------------------------------------------------------------------------")
    print("Функция: f(x)=2^{-x} - sin(x)")
    print("Отрезок [A;B] поиска корней нечетной кратности уравнения f(x)=0: [-5;10]")
    print("Точность: 1e-6")
    print("--------------------------------------------------------------------------")

    # Цикл работает, пока пользователь не перестанет начинать заново.
    while True:
        a = float(input("Введите левую границу отрезка A (целое число): "))
        b = float(input("Введите правую границу отрезка B (целое число): "))

        # Цикл работает, пока пользователь не будет доволен выбором N.
        while True:
            n = int(input("Введите число сегментов отрезка N (целое положительное число >= 2): "))

            segments = segmentation(f, a, b, n)

            print("--------------------------------------------------------------------------")
            print(f"Найдено {len(segments)} отрезка(-ов), содержащих корни нечетной кратности.")

            for i, segment in enumerate(segments, start=1):
                print(i, segment)

            print("--------------------------------------------------------------------------")
            prompt = input("Хотите поменять значение N? [y/n]: ")
            if prompt.strip().lower() in set_no:
                break

        # Цикл работает, пока пользователь не будет доволен выбором epslion.
        while True:
            print("--------------------------------------------------------------------------")

            abs_tol = float(input("Введите точность: "))

            print("--------------------------------------------------------------------------")
            
            segment_choice = int(
                input("Выберите номер промежутка для поиска приближения корня (или 0 для выбора всех промежутков): "))

            match segment_choice:
                case 0:
                    for segment in segments:
                        printer(segment, abs_tol)
                case i:
                    if i >= len(segments):
                        print(f"Сегмент с номером {i} не существует")
                    else:
                        printer(segments[i - 1], abs_tol)

            prompt = input("Хотите поменять значение epsilon? [y/n]: ")
            if prompt.strip().lower() in set_no:
                break

        prompt = input("Хотите начать заново с выбора границ отрезка? [[y/n]: ")
        if prompt.strip().lower() in set_no:
            break

    return 0


if __name__ == "__main__":
    if (main() == 0):
        print("Программа успешно завершена")
