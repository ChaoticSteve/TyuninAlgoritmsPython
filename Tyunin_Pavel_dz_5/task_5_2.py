'''
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом
каждое число представляется как массив, элементы которого это цифры числа. Например,
пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
'''
a = list(input('Введите первое число в шестандцетиричном виде: ').strip().upper())
b = list(input('Введите первое число в шестандцетиричном виде: ').strip().upper())
print(a, b)
amount = list(f'{int("".join(a), base=16) + int("".join(b), base=16):X}'.strip())
print(f'Их сумма: {amount}')
multiply = list(f'{int("".join(a), base=16) * int("".join(b), base=16):X}'.strip())
print(f'Их произведение: {multiply}')