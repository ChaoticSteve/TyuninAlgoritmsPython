'''
Определить, какое число в массиве встречается чаще всего.
'''

from random import randint

numbers_list = [randint(1, 10) for _ in range(0, 15)]
counter = []
for number in numbers_list:
    counter.append(numbers_list.count(number))
print(f'Наиболее часто встречается {numbers_list[counter.index(max(counter))]}. Всего {max(counter)} раз(а)')
