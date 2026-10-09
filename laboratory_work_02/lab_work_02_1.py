# Вариант 5

try:
    x = float(input('Введите значение аргумента X: '))
    y = 0.0
except ValueError:
    print("\n")
    print('Аргумент X должен быть числом!')
    print('Попробуйте еще раз, введя корректный аргумент X')
else:
    if -4 <= x <= -2:
        y = x + 3
    elif -2 < x <= 4 :
        y = -x / 2
    elif 4 < x <= 6:
        y = -2
    elif 6 < x <= 10:
        y = (4 - (x - 8) ** 2) ** (1 / 2) - 2
    else:
         print("\n")
         print(f'Функция Y(X) не определена при значении аргумента X = {x:.2f}')

    print("\n")
    print(f'Y = {y:.2f}, при X = {x:.2f}')
