# По длинам трех отрезков, введенных пользователем,
# определить возможность существования треугольника, составленного из этих отрезков.
# Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.

a, b, c = map(int, input('Введите длины сторон треугольника через ",": ').split(','))
if a + b < c or a + c < b or b + c < a:
    print('Такого треугольника не существует')
elif a == b == c:
    print('Это равносторонний')
elif a == b or b == c or a == c:
    print('Это равнобедренный')
else:
    print('Это разносторонний')