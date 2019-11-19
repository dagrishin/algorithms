"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""


def progression_amount(n):
    if n == 1:
        return 1
    return n + progression_amount(n - 1)


try:
    n = int(input('Введите n (n целое >0): '))
    print('Верно' if float(progression_amount(n)) == float(n * (n + 1) / 2) else 'не верно' )
except ValueError:
    print('Неправельный ввод')
