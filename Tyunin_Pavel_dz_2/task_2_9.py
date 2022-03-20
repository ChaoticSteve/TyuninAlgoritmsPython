'''
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
'''


def digit_sum(num):
    digits_list = []
    while num != 0:
        digits_list.append(num % 10)
        num //= 10
    return sum(digits_list)


numbers = list(map(int, input('Введите через запятую несколько натуральных чисел: ').split(',')))
dict_num = {}
for number in numbers:
    dict_num[digit_sum(number)] = number
print(f'Наибольшее число: {dict_num.get(max(dict_num.keys()))}. Сумма его цифр {max(dict_num.keys())}')
