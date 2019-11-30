"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import Counter, deque

s = '0123456789ABCDEF'
a = deque(input())
b = deque(input())
number = Counter(s)
alphabet = deque(s)
j = 0
for key, value in number.items():
    number[key] = j
    j += 1


def suma(number_1, number_2):
    ost = 0
    amount = deque()
    while len(number_1) or len(number_2):
        c = number_1.pop() if len(number_1) else 0
        d = number_2.pop() if len(number_2) else 0
        s = number[c] + number[d] + ost
        if s >= 16:
            amount.appendleft(alphabet[(s % 16)])
            ost = s // 16
        else:
            amount.appendleft(alphabet[s])
            ost = 0
    if ost != 0:
        amount.appendleft(ost)
    return amount


# Сложение
print('Сумма = ', suma(a.copy(), b.copy()))
# Умножение
ost = 0
amount_fin = ['0']
i = len(a) - 1
j = len(b) - 1
while i >= 0:
    c = a[i]
    j = len(b) - 1
    amount = deque('0'*(len(a)-i-1))
    ost = 0
    while j >= 0:
        d = b[j]
        s = number[c] * number[d] + ost
        if s >= 16:
            amount.appendleft(alphabet[(s % 16)])
            ost = s // 16
        else:
            amount.appendleft(alphabet[s])
            ost = 0
        j -= 1
    i -= 1
    if ost != 0:
        amount.appendleft(alphabet[ost])
    amount_fin = suma(amount_fin, amount)
print(ost)
print('Произведение', amount_fin)
