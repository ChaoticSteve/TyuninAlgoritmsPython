'''
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
'''
from random import randint

numbers_list = [randint(1, 20) for _ in range(0, 20)]
index_min = numbers_list.index(min(numbers_list))
index_max = numbers_list.index(max(numbers_list))
print(f'Сумма элементов {sum([numbers_list[i] for i in range(index_min + 1, index_max)])}')