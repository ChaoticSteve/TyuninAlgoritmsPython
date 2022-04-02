from memory_profiler import profile


@profile
def task_3_8():
    def matrix_fill():
        result = list(map(int, input('Введите 4 элемента матрицы через ",": ').split(',')))
        result.append(sum(result))
        return result

    print(f'{matrix_fill()}\n{matrix_fill()}\n{matrix_fill()}\n{matrix_fill()}\n')


'''
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
     4     19.4 MiB     19.4 MiB           1   @profile
     5                                         def task_3_8():
     6     19.4 MiB      0.0 MiB           5       def matrix_fill():
     7     19.4 MiB      0.0 MiB           4           result = list(map(int, input('Введите 4 элемента матрицы через ",": ').split(',')))
     8     19.4 MiB      0.0 MiB           4           result.append(sum(result))
     9     19.4 MiB      0.0 MiB           4           return result
    10                                         
    11     19.4 MiB      0.0 MiB           1       print(f'{matrix_fill()}\n{matrix_fill()}\n{matrix_fill()}\n{matrix_fill()}\n')



Process finished with exit code 0
'''


# task_3_8()


@profile
def task_1_1():
    from math import prod

    number = input('Введите 3-х значное число: ')
    numbers = []
    i = 0
    for i in range(len(number)):
        numbers.append(int(number[i]))
    print(sum(numbers))
    print(prod(numbers))


'''
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    35     19.3 MiB     19.3 MiB           1   @profile
    36                                         def task_1_1():
    37     19.3 MiB      0.0 MiB           1       from math import prod
    38                                         
    39     19.3 MiB      0.0 MiB           1       number = input('Введите 3-х значное число: ')
    40     19.3 MiB      0.0 MiB           1       numbers = []
    41     19.3 MiB      0.0 MiB           1       i = 0
    42     19.3 MiB      0.0 MiB           4       for i in range(len(number)):
    43     19.3 MiB      0.0 MiB           3           numbers.append(int(number[i]))
    44     19.3 MiB      0.0 MiB           1       print(sum(numbers))
    45     19.3 MiB      0.0 MiB           1       print(prod(numbers))



Process finished with exit code 0
'''


# task_1_1()


@profile
def task_4_2():
    import time
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
    print(f'Число: {simple_eratosthenes(5, 100)}\n'
          f'Время: {time.time() - time_start}')


'''
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    69     19.4 MiB     19.4 MiB           1   @profile
    70                                         def task_4_2():
    71     19.4 MiB      0.0 MiB           1       import time
    72     19.4 MiB      0.0 MiB           2       def simple_eratosthenes(position, border):
    73     19.4 MiB      0.0 MiB           1           position_simple = 0
    74     19.4 MiB      0.0 MiB         103           sequence = [num for num in range(0, border)]
    75     19.4 MiB      0.0 MiB           1           sequence[1] = 0
    76     19.4 MiB      0.0 MiB           1           p = 2
    77     19.4 MiB      0.0 MiB          99           while p < border:
    78     19.4 MiB      0.0 MiB          98               if sequence[p] != 0:
    79     19.4 MiB      0.0 MiB          25                   i = p * 2
    80     19.4 MiB      0.0 MiB         169                   while i < border:
    81     19.4 MiB      0.0 MiB         144                       sequence[i] = 0
    82     19.4 MiB      0.0 MiB         144                       i += p
    83     19.4 MiB      0.0 MiB          98               p += 1
    84     19.4 MiB      0.0 MiB          12           for num in sequence:
    85     19.4 MiB      0.0 MiB          12               if num != 0:
    86     19.4 MiB      0.0 MiB           5                   position_simple += 1
    87     19.4 MiB      0.0 MiB          12               if position_simple == position:
    88     19.4 MiB      0.0 MiB           1                   return num
    89                                         
    90     19.4 MiB      0.0 MiB           1       time_start = time.time()
    91     19.4 MiB      0.0 MiB           2       print(f'Число: {simple_eratosthenes(5, 100)}\n'
    92     19.4 MiB      0.0 MiB           1             f'Время: {time.time() - time_start}')



Process finished with exit code 0
'''

# task_4_2()

# Python 3.9
# Windows 10 x64
