'''Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).'''

number = input('Введите натуральное число: ')
even_list = []
odd_list = []
even_i = 0
odd_i = 0
for num in number:
    if int(num) % 2 == 0:
        even_i += 1
        even_list.append(int(num))
    else:
        odd_i += 1
        odd_list.append(int(num))
print(f'В числе {int(number)}: {even_i} чет. {even_list} и {odd_i} нечет. {odd_list}')
