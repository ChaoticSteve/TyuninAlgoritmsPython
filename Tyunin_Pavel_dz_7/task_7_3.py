'''
Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные
части: в одной находятся элементы, которые не меньше медианы, в другой – не больше
медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком
сложно, то используйте метод сортировки, который не рассматривался на уроках
'''

import random


def get_median(array, pivot_fn=random.choice):
    if len(array) % 2 == 1:
        return subpart(array, len(array) / 2, pivot_fn)
    else:
        return 0.5 * (subpart(array, len(array) / 2 - 1, pivot_fn) +
                      subpart(array, len(array) / 2, pivot_fn))


def subpart(array, k, pivot_fn):
    pivot = pivot_fn(array)
    lows = [el for el in array if el < pivot]
    highs = [el for el in array if el > pivot]
    pivots = [el for el in array if el == pivot]
    if k < len(lows):
        return subpart(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return subpart(highs, k - len(lows) - len(pivots), pivot_fn)


m = 50
array = [random.randint(-100, 100) for _ in range(2 * m + 1)]
print(array)
print(get_median(array))