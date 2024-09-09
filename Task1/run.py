from solution import f, df, segmentation, bisection, newton, modified_newton, secant


set_yes = {"yes", "да", "y"}

set_no = {"no", "нет", "n"}


def main():
    print("Численные методы решения нелинейных уравнений")
    print("Исходные параметры тестовой задачи")
    print("--------------------------------------------------------------------------")
    print("Функция: f(x)=2^{-x} - sin(x)")
    print("Отрезок [A;B] поиска корней нечетной кратности уравнения f(x)=0: [-5;10]")
    print("Точность: 1e-6")
    print("--------------------------------------------------------------------------")

    a = float(input("Введите левую границу отрезка A: "))
    b = float(input("Введите правую границу отрезка B: "))

    # Цикл работает, пока пользователь не будет доволен выбором N.
    while True:
        n = int(input("Введите число сегментов отрезка N: "))

        segments = segmentation(f, a, b, n)

        for i, segment in enumerate(segments, start=1):
            print(i, segment)

        print(
            f"Найдено {len(segments)} отрезка(-ов), содержащих корни нечетной кратности."
        )

        prompt = input("Хотите поменять значение N?: ")

        if prompt.strip().lower() in set_no:
            break

    # Цикл работает, пока пользователь не будет доволен выбором epslion.
    while True:
        abs_tol = float(input("Введите точность: "))

        segment_choice = int(
            input(
                "Выберите номер промежутка для поиска приближения корня (0 для выбора всех промежутков): "
            )
        )

        match segment_choice:
            case 0:
                for segment in segments:
                    print(segment)
            case i:
                print(segments[i - 1])

        prompt = input("Хотите поменять значение epsilon?: ")

        if prompt.strip().lower() in set_no:
            break

    return 0


if __name__ == "__main__":
    main()
