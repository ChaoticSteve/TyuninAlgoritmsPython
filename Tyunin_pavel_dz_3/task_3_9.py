'''
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
'''

import random

rnd_mtx = [[random.randrange(1, 10) for _ in range(0, 5)] for _ in range(0, 5)]
min_list = [min(elem_list) for elem_list in rnd_mtx]
print('В матрице:')
for elem_list in rnd_mtx:
    print(elem_list)
print(f'Максимальный элемент среди минимальных элементов: {max(min_list)}.')