# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number = input('Введите трехзначное число')
if number.isdigit():
    number = int(number)
    hundreds = number // 100
    if hundreds > 9 or hundreds < 1:
        print('Вы ввели не трехзначное число')
    else:
        dozens = (number % 100) // 10
        units = (number % 100) % 10
        print('Сумма:', hundreds + dozens + units, 'Произведение:', hundreds * dozens * units)
else:
    print('Вы ввели не трехзначное число')
