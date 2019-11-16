"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""

from random import random

left_border = int(input("Нижняя граница: "))
right_border = int(input("Верхняя граница: "))
number = int(random() * (right_border - left_border + 1)) + left_border
print(number)


left_border = int(input("Нижняя граница: "))
right_border = int(input("Верхняя граница: "))
number = random() * (right_border - left_border) + left_border
print(number)

left_border = input("Нижняя граница: ")
left_border = ord(left_border)
right_border = input("Верхняя граница: ")
right_border = ord(right_border)
number = int(random() * (right_border - left_border + 1)) + left_border
print(chr(number))
