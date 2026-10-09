import numpy as np

def SumColsWithoutNeg(Matr):
    (nRow, nCol) = Matr.shape
    total_sum = 0
    found = False

    for Col in range(nCol):
        negative = False
        col_sum = 0
        for Row in range(nRow):
            if Matr[Row][Col] < 0:
                negative = True
            col_sum += Matr[Row][Col]

        if not negative:
            total_sum += col_sum
            found = True

    return (total_sum, found)

def MinAbsSumParallelSecondary(Matr):
    (nRow, nCol) = Matr.shape
    min_sum = None

    for k in range(2 * nRow - 1):
        current_sum = 0
        for i in range(nRow):
            j = k - i
            if 0 <= j < nCol:
                val = Matr[i][j]
                abs_val = val if val >= 0 else -val
                current_sum += abs_val

        if min_sum is None or current_sum < min_sum:
            min_sum = current_sum

    return min_sum

fh_i = open("lab5_in.txt", "rt")
MyMatr = np.loadtxt(fh_i, dtype=int, ndmin=2)
fh_i.close()

(col_sum, is_found) = SumColsWithoutNeg(MyMatr)
if is_found:
    res1 = "Сумма в столбцах без отриц. чисел: {0}".format(col_sum)
else:
    res1 = "Столбцов без отрицательных элементов не найдено."

min_diag_sum = MinAbsSumParallelSecondary(MyMatr)
res2 = "Минимум сумм модулей диагоналей, паралл. побочной: {0}".format(min_diag_sum)

fh_o = open("lab5_ou.txt", "wb")
str_header = 'Исходная матрица:'

fstr = " ".join(('\n', res1, '\n', res2))

np.savetxt(fh_o, MyMatr, fmt='%4d', header=str_header, footer=fstr, comments='', encoding='utf-8')

fh_o.close()