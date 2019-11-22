"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""


def revers(number):
    if len(str(number)) == 1:
        return str(number)
    return str(number % 10) + revers(number // 10)


try:
    print(revers(int(input('Введите целое число: '))))

except ValueError:
    print('Введено не целое число')
