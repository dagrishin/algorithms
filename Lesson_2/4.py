"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


def progression_amount(n):
    if n == 1:
        return 1
    return (-1 / 2)**(n - 1) + progression_amount(n - 1)


try:
    print(progression_amount(int(input('Введите n (n целое >0): '))))
except ValueError:
    print('Неправельный ввод')
