"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""


def sum_of_digits(number):
    if len(str(number)) == 1:
        return number
    return number % 10 + sum_of_digits(number // 10)


n = 3
result = 0

for i in range(n):
    number = int(input(f'Введите число {i + 1}: '))
    sum_number = sum_of_digits(number)
    if result < sum_number:
        desired_number = number
        result = sum_number

print(desired_number, result)
