'''
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
'''

import random

def merger_sort(array, start=0, end=None):
    def subpart(array, start, end, pivot_index):
        array[start], array[pivot_index] = array[pivot_index], array[start]
        pivot = array[start]
        idx1 = start + 1
        idx2 = start + 1

        while idx2 <= end:
            if array[idx2] <= pivot:
                array[idx2], array[idx1] = array[idx1], array[idx2]
                idx1 += 1
            idx2 += 1

        array[start], array[idx1 - 1] = array[idx1 - 1], array[start]
        return idx1 - 1

    if end is None:
        end = len(array) - 1
    if end - start < 1:
        return

    pivot_index = (start + end) // 2
    x = subpart(array, start, end, pivot_index)
    merger_sort(array, start, x - 1)
    merger_sort(array, x + 1, end)

array = [random.randint(0,50) for _ in range(100)]
print(f'Исходный список:\n {array}')
merger_sort(array)
print(f'Отсортированный список:\n {array}')