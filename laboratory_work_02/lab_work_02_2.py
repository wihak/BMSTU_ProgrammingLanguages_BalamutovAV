# Вариант 5

try:
    r = float(input('Введите значение R: '))
    x = float(input('Введите значение X: '))
    y = float(input('Введите значение Y: '))
except ValueError:
    print('\nАргументы R, X, Y должны быть числом!')
    print('Попробуйте еще раз, введя корректные аргументы R, X, Y')
else:
    if r < 0:
        print('Радиус не может быть отрицательным!')
    else:
        in_area = False
        if (((x >= 0 and y >= 0) or (x <= 0 and y <= 0)) and (x ** 2 + y ** 2 <= r ** 2)) or (x <= 0 and y >= 0 and (y <= x + r)):
            in_area = True
        if in_area:
            print(f'\nТочка ({x:.2f}, {y:.2f}) попадает в область!')
        else:
            print(f'\nТочка ({x:.2f}, {y:.2f}) не попадает в область!')

