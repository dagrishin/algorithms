"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""

from random import random
number = int(random() * 100)
print(number)

for i in range(10):
    p = True
    while p:
        try:
            user_number = int(input('Введите число: '))
            p = False
        except ValueError:
            print('Вы ввели не корректное число')
    if number == user_number:
        print('Вы угодали')
        break
    elif number > user_number:
        print('Больше')
    else:
        print('Меньше')
    if i == 9:
        print('Вы проиграли')
