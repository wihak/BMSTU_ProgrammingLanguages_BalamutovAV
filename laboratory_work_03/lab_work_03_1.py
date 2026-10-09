# Вариант 5
from math import *

print('\nФункция определена при -4 <= X <= 10\n')

try:
    xb = float(input('Введите Xbeg='))
    xe = float(input('Введите Xend='))
    dx = float(input('Введите Dx='))
except ValueError:
    print('\nЗначения аргументов должны быть числами!')
    print('Повторно выполните запустите программу и введите данные корректно!\n')
else:
    if dx == 0:
        print('\nШаг Dx не должен быть равен 0!')
    elif xe == xb:
        print("\nНачальный и конечный значения X должны различаться!")
    elif abs(xe - xb) < dx:
        print("\nШаг слишком большой!")
    elif ((xe > xb) and dx > 0) or ((xb > xe) and dx < 0):
        xt = xb

        print("\n+-----------+-----------+")
        print("I     X     I     Y     I")
        print("+-----------+-----------+")

        while xt != xe + dx:
            flag = 0
            if -4 <= xt <= -2:
                y = xt + 3
            elif -2 < xt <= 4 :
                y = -xt / 2
            elif 4 < xt <= 6:
                y = -2
            elif 6 < xt <= 10:
                y = (4 - (xt - 8) ** 2) ** (1 / 2) - 2
            else:
                y = ' не опр. '
                flag = 1

            if flag:
                print(f'I {xt:^9.4f} I {y} I')
            else:
                print(f'I {xt:^9.4f} I {y:^9.4f} I')

            xt += dx

        print("+-----------+-----------+")

    else:
        print('\nНекорректные данные!')
