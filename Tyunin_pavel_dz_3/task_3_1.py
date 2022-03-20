'''
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
'''


def multiplicity(num):
    result = []
    number = [n for n in range(2, 100)]
    for n in number:
        if n % num == 0:
            result.append(n)
    return result


numbers = [n for n in range(2, 10)]
for num in numbers:
    print(f'Числу {num} кратны {len(multiplicity(num))} чисел в диапозоне 2-99')
