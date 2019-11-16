# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

number1 = float(input('number1 = '))
number2 = float(input('number2 = '))
number3 = float(input('number3 = '))

if number1 == number2 or number1 == number3:
    print(number1)
elif number2 == number3:
    print(number2)

if number1 > number2 > number3 or number1 < number2 < number3:
    print(number2)
if number2 > number1 > number3 or number2 < number1 < number3:
    print(number1)
if number2 > number3 > number1 or number2 < number3 < number1:
    print(number3)




