import random
def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    else:
        middle = int(len(arr) / 2)
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left) > 0:
        result.extend(left)
    if len(right) > 0:
        result.extend(right)
    return result

n = int(input("Введите размер строки квадратной матрицы: "))
matrix = [[random.randint(-1000, 1000) for i in range(n)] for j in range(n)]
for arr in matrix:
    print(*arr)
print()
for i in range(n):
    print(*merge_sort(matrix[i]))
