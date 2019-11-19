"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""

number = input('Введите натуральное число: ')
even = 0
not_even = 0
try:
    int(number)
    for numeral in number:
        if int(numeral) % 2 == 0:
            even += 1
        else:
            not_even += 1
    print(even, not_even)

except ValueError:
    print('Введено не натуральное число')

