# Вариант 5
from random import uniform

try:
    r = float(input('Введите значение R: '))
except ValueError:
    print('\nЗначение R должно быть числом!')
    print('Попробуйте еще раз, введя корректные аргументы')

if r < 0:
    print('Радиус не может быть отрицательным!')
else:
    print("\n+-----------+-----------+-----------+")
    print("I     X     I     Y     I    RES    I")
    print("+-----------+-----------+-----------+")
    flag = False
    for _ in range(10):
        x = uniform(-r, r)
        y = uniform(-r, r)

        if (((x >= 0 and y >= 0) or (x <= 0 and y <= 0)) and (x ** 2 + y ** 2 <= r ** 2)) or (x <= 0 and y >= 0 and (y <= x + r)):
            flag = True
        else:
            flag = False

        print(f'I {x:9.4f} I {y:9.4f} I', end='')

        if flag:
            print('    Yes    I')
        else:
            print('    No     I')

    print("+-----------+-----------+-----------+")
