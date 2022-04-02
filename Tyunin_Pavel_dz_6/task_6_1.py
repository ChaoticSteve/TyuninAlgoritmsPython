from memory_profiler import profile


@profile
def task_3_8():
    def matrix_fill():
        result = list(map(int, input('Введите 4 элемента матрицы через ",": ').split(',')))
        result.append(sum(result))
        return result

    print(f'{matrix_fill()}\n{matrix_fill()}\n{matrix_fill()}\n{matrix_fill()}\n')


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
# task_4_2()

# Python 3.9
# Windows 10 x64
