'''
Написать два алгоритма нахождения i-го по счёту простого числа.

    Без использования «Решета Эратосфена»;
    Используя алгоритм «Решето Эратосфена»
'''
import time

# Самый медленный вариант
def find_simple(position):
    simple = 2
    i = 1
    check_number = 2
    while i <= position:
        for num in range(2, check_number - 1):
            if not check_number % num:
                break
        else:
            simple = check_number
            i += 1
        check_number += 1
    return simple


time_start = time.time()
print(f'Число: {find_simple(10000)}\n'
      f'Время: {time.time() - time_start}')

'''Столкнулся с проблемой, что для начала нужно просчитать простые числа используя «Решето Эратосфена» с запасом,
только потом выдать нужное число. Пришло в голову 2 варианта поиска нужного числа.
'''


# Немного медленней

def simple_eratosthenes(position, border):
    sequence = [num for num in range(0, border)]
    sequence[1] = 0
    p = 2
    while p < border:
        if sequence[p] != 0:
            i = p * 2
            while i < border:
                sequence[i] = 0
                i += p
        p += 1
    return sorted(list(set(sequence)))[position]


time_start = time.time()
print(f'Число: {simple_eratosthenes(10000, 10 ** 6)}\n'
      f'Время: {time.time() - time_start}')

# Самый быстрый

def simple_eratosthenes(position, border):
    position_simple = 0
    sequence = [num for num in range(0, border)]
    sequence[1] = 0
    p = 2
    while p < border:
        if sequence[p] != 0:
            i = p * 2
            while i < border:
                sequence[i] = 0
                i += p
        p += 1
    for num in sequence:
        if num != 0:
            position_simple += 1
        if position_simple == position:
            return num


time_start = time.time()
print(f'Число: {simple_eratosthenes(10000, 10 ** 6)}\n'
      f'Время: {time.time() - time_start}')
