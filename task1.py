import random
from time import perf_counter
size = int(input("Введите размер списка: "))
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
    return arr
arr = [random.randint(-1000, 1000) for i in range(size)]
tic = perf_counter()
print(bubble_sort(arr))
toc = perf_counter()
print(f"Время пузырьковой сортировки: {toc - tic}\nСложность O(n^2)")
tic = perf_counter()
print(sorted(arr))
toc = perf_counter()
print(f"Время встроенной сортировки: {toc - tic}\nСложность O(n)")
