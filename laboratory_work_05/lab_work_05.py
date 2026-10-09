import numpy as np

def MakeMatr(n, a, b):

    Matr = np.random.randint(a, b + 1, size=(n, n))
    return Matr


def PrintMatr(Matr):
    (nRow, nCol) = Matr.shape
    for Row in range(nRow):
        for Col in range(nCol):
            print("{0:4d}".format(Matr[Row][Col]), end=" ")
        print()
    print()


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



n = int(input("Введите размер целочисленной матрицы (NxN): "))

MyMatr = MakeMatr(n, -10, 10)

print("Исходная матрица:")
PrintMatr(MyMatr)

# 1
(col_sum, is_found) = SumColsWithoutNeg(MyMatr)
if is_found:
    print("Сумма элементов в столбцах без отрицательных чисел: {0}".format(col_sum))
else:
    print("Столбцов без отрицательных элементов не найдено.")

# 2
min_diag_sum = MinAbsSumParallelSecondary(MyMatr)
print("Минимум сумм модулей элементов диагоналей, параллельных побочной: {0}".format(min_diag_sum))