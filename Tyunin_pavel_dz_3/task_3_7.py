'''
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
'''
from random import randint

numbers_list = [randint(1, 20) for _ in range(0, 20)]
print(f'Два наименьших элемента: {sorted(numbers_list)[0]}, {sorted(numbers_list)[1]}')