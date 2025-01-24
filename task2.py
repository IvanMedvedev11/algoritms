import random
def cycle_shift(arr):
    last_elem = arr[-1]
    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = last_elem
    return arr
n = int(input("Введите размер стороны квадратной матрицы: "))
matrix = [[random.randint(-1000, 1000) for i in range(n)] for j in range(n)]
for arr in matrix:
    print(*arr)
print()
for i in range(len(matrix)):
    print(*cycle_shift(matrix[i]))
