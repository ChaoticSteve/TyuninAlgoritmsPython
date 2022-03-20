'''
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
'''
import random

numbers_list = [random.randrange(-15, 10) for _ in range(0, 20)]
print(f'Наименьшее число {min(numbers_list)}, его индекс {numbers_list.index(min(numbers_list))}')