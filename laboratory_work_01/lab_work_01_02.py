# Вариант 5
from math import sin, cos

a = float(input('Введите значение a: '))


z1 = 1 - 1 / 4 * sin(2 * a) ** 2  + cos(2 * a)
z2 = cos(a) ** 2 + cos(a) ** 4

print('\n')
print(f'z1 = {z1:.4f}, при a = {a:.2f}')
print(f'z2 = {z2:.4f}, при a = {a:.2f}')
