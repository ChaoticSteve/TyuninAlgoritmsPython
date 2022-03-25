'''
Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
'''

# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

import time

n = int(input('Введите длинну ряда чисел: '))
time_start = time.time()
num_list = []
i = 1
for _ in range(n):
    num_list.append(i)
    i /= -2
print(f'Их сумма: {sum(num_list)}\n'
      f'Время: {time.time() - time_start}')

n = int(input('Введите длинну ряда чисел: '))
time_start = time.time()
i = 1
result = 0
for _ in range(n):
    result += i
    i /= -2
print(f'Сумма: {result}\n'
      f'Время: {time.time() - time_start}')

# Самое долгое решение
n = int(input('введите натуральное число: '))
time_start = time.time()
result = 0
for number in range(n):
    if number % 2:
        result += (-1 ** (number - 1)) / 2 ** number
    else:
        result += (1 ** (number - 1)) / 2 ** number
print(f'Их сумма: {result}\n'
      f'Время: {time.time() - time_start}')
