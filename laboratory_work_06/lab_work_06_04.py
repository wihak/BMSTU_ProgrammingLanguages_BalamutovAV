fi = open("lab4_in.txt", "rt")

arr = [float(x) for x in fi.readline().split()]

a = float(fi.readline().strip())
b = float(fi.readline().strip())

fi.close()

max_elem = max(arr)
last_pos_index = -1
for i in range(len(arr)):
    if arr[i] > 0:
        last_pos_index = i

fo = open("lab4_ou.txt", "wt")

fo.write("Начальное состояние: {0}\n".format(arr))
fo.write("Границы: a = {0}, b = {1}\n\n".format(a, b))

if last_pos_index == -1:
    fo.write("Отсутствует положительное значение в массиве.\n")
elif a > b:
    fo.write("Ошибка: Значение a должно быть больше b.\n")
else:
    sum_elem = sum(arr[:last_pos_index])
    
    result = []
    for elem in arr:
        if not (a <= abs(elem) <= b):
            result.append(elem)
            
    result += [0.0] * (len(arr) - len(result))

    fo.write("1) Максимальный элемент списка: {0}\n".format(max_elem))
    fo.write("2) Сумма элементов до последнего положительного: {0}\n".format(sum_elem))
    fo.write("Конечное состояние списка: {0}\n".format(result))

fo.close()