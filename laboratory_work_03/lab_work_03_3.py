# Вариант 5

try:
    xb = float(input('Введите Xbeg (|x| < 1) : '))
    xe = float(input('Введите Xend (|x| < 1) : '))
    dx = float(input('Введите Dx: '))
    eps = float(input('Введите Eps: '))
except ValueError:
    print('\nЗначения Xbeg, Xend, Dx, Eps должны быть числом!')
    print('Попробуйте снова!')

else:
    if abs(xb) >= 1 or abs(xe) >= 1:
        print('\nБудьте внимательны, |x| < 1 ')
        print('Попробуйте снова!')

    elif xe < xb:
        print('\nНачальное значение должно быть меньше конечного!')

    elif xe - xb < dx:
        print('\nСлишком большой шаг Dx!')

    elif eps <= 0:
        print('\nНекорректное значение эпсилон!')

    else:
        print("\n+-----------+-----------+-----------+")
        print("I     X     I     Y     I     N     I")
        print("+-----------+-----------+-----------+")

        xt = xb

        while xt <= xe:
            an = 2 * xt
            n = 0
            y = an
            while True:
                k = (xt ** 2) * (2 * n + 1) / (2 * n + 3)
                an = an * k
                y = y + an
                n = n + 1
                if abs(an) < eps:
                    break
            print("I {0: 9.4f} I {1: 9.4f} I {2: ^9} I".format(xt, y, n))
            xt = xt + dx

        print("+-----------+-----------+-----------+")

