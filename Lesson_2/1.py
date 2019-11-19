"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""

while True:
    number1 = input('number1 = ')
    sign = ''
    b = True
    p = True
    while b:
        if sign == '':
            sign = input('sign: ')

        if sign == '0':
            p = False
            break
        if sign not in '+-*/' or len(sign) != 1:
            print('sign error')
            sign = ''
        else:
            b = False
    if p == False:
        break
    number2 = input('number2 = ')

    if sign == '+':
        print(f'{number1} {sign} {number2} = {int(number1) + int(number2)}')
    if sign == '-':
        print(f'{number1} {sign} {number2} = {int(number1) - int(number2)}')
    if sign == '*':
        print(f'{number1} {sign} {number2} = {int(number1) * int(number2)}')
    if sign == '/':
        if number2 == '0':
            print('На ноль делить нельзя')
        else:
            print(f'{number1} {sign} {number2} = {int(number1) / int(number2)}')
