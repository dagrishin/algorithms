"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

from collections import namedtuple, defaultdict

party = {}
s = defaultdict(float)
group_values = defaultdict(float)
Company = namedtuple(
    'Company',
    'quarter, bailout, average_revenue'
)

n = int(input('Количество предприяий = '))

for i in range(n):
    name = input('name: ')
    quarter = []
    for j in range(4):
        quarter.append(float(input(f'{j + 1} квартал = ')))
        s[name] += quarter[j]
    group_values[0] += s[name]
    average_revenue = s[name] / 4
    company = Company(quarter, s[name], average_revenue)
    party[name] = company
group_values[1] = group_values[0] / (4 * n)
print(party)

condition = defaultdict(list)
for name, company in party.items():
    if company.average_revenue < group_values[1]:
        condition['unprofitable'] += name
    else:
        condition['profitable'] += name
print(condition)
