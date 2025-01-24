import random
from time import perf_counter
def enumeration(arr):
    res = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > res:
            res = arr[i]
    return res
def bubble_sort(arr):
    unordered = True
    n = len(arr)
    while unordered:
        unordered = False
        for i in range(n - 1):
            if(arr[i]>arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                unordered = True
        n -= 1
    return arr[-1]
n = int(input("Введите размер списка: "))
arr = [random.randint(-1000, 1000) for i in range(n)]
print(*arr)
tic = perf_counter()
print(enumeration(arr))
toc = perf_counter()
print(f"Время перебора: {toc - tic}")
tic = perf_counter()
print(bubble_sort(arr))
toc = perf_counter()
print(f"Время пузырьковой сортировки: {toc - tic}")
