# Пользователь вводит данные о количестве предприятий, их наименования
# и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше и ниже среднего.

from collections import namedtuple, deque

periods = 4
Company = namedtuple('Company', ['name', 'quarters', 'profit'])
all_companies = set()

num = int(input("Сколько у вас компаний? "))
total_profit = 0
for i in range(1, num + 1):
    profit = 0
    quarters = []
    name = input(f'Введите имя компании {i}: ')

    for j in range(periods):
        quarters.append(int(input(f'Прибыль за {j + 1}-й квартал: ')))
        profit += quarters[j]

    comp = Company(name=name, quarters=tuple(quarters), profit=profit)

    all_companies.add(comp)
    total_profit += profit

average = total_profit / num

print(f'\nСредняя прибыль вашей группы компаний: {average}')

print(f'\nКомпании с прибылью выше среднего:')
for comp in all_companies:
    if comp.profit > average:
        print(f'Компания {comp.name} заработала {comp.profit}')


print(f'\nОтстающие компании:')
for comp in all_companies:
    if comp.profit < average:
        print(f'{comp.name} получила прибыль ниже среднего: {comp.profit}')