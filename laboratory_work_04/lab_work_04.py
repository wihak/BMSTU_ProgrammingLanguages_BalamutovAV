# Вариант 5
from random import *

n = int(input("Задайте количество элементов в массиве (N<=30) N: "))
if n > 30:
    n = 30
elif n < 5:
    n = 5



arr = []
for i in range(n):
    arr.append(uniform(-5, 5))
print(f'\nНачальное состояние: {arr}\n')

max_elem = max(arr)

last_pos_index = -1
for i in range(len(arr)):
    if arr[i] > 0:
        last_pos_index = i

if last_pos_index == -1:
    print('\nСгенерируйте список еще раз, отсутсвует положительное значение')

else:
    sum_elem = 0

    for i in range(0, last_pos_index, 1):
        sum_elem += arr[i]

    a = float(input('Введите значение a (левая граница): '))
    b = float(input('Введите значение b (правая граница): '))

    if a > b:
        print('Значение a должно быть больше b')
    else:
        result = []
        for elem in arr:
            if not (a <= abs(elem) <= b):
                result.append(elem)

        result += [0.0] * (n - len(result))

        print(f'\n1) Максимальный элемент списка: {max_elem}')
        print(f'\n2) Сумма элементов до последнего положительного значения: {sum_elem}')
        print(f'\nКонечное состояние списка: {result}\n')

