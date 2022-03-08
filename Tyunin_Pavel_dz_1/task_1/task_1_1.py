# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
from math import prod

number = input('Введите 3-х значное число: ')
numbers = []
i = 0
for i in range(len(number)):
    numbers.append(int(number[i]))
print(sum(numbers))
print(prod(numbers))