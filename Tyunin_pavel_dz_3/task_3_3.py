'''
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''
from random import randint

numbers_list = [randint(1, 100) for _ in range(0, 20)]
print(numbers_list)
index_max, index_min = numbers_list.index(max(numbers_list)), numbers_list.index(min(numbers_list))
numbers_list[index_max], numbers_list[index_min] = numbers_list[index_min], numbers_list[index_max]
print(numbers_list)
