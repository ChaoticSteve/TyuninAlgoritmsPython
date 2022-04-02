'''
Пользователь вводит данные о количестве предприятий, их наименования
и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести
наименования предприятий, чья прибыль ниже среднего.
'''

def get_average(values):
    amount = 0
    for value in values:
        amount += sum(value)
    return amount/len(values)

company = {}
count = int(input('Количество предприятий: '))
for i in range(count):
    name_company = input('Введите название предприятия: ')
    income_company = list(map(float,input('Введите прибыль за 4 квартала через ",": ').split(',')))
    company[name_company] = income_company
average = get_average(company.values())
print(f'Среднее: {average}')
print('Выше среднего:')
for key, value in company.items():
    if sum(value) > average:
        print(f'{key}, годовой доход: {sum(value)}')
print('Ниже среднего:')
for key, value in company.items():
    if sum(value) < average:
        print(f'{key}, годовой доход: {sum(value)}')