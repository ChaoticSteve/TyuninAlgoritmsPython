'''
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и
отсортированный массивы. Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее).
'''

import random


def bubble_sort(array):
    sort_sub_cnt = 1
    while sort_sub_cnt < len(array):
        check = False
        for i in range(len(array) - sort_sub_cnt):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                check = True
        sort_sub_cnt += 1
        if not check:
            break


array = [random.randint(-100, 100) for _ in range(100)]
print(f'Исходный список:\n {array}')
bubble_sort(array)
print(f'Отсортированный список:\n {array}')
