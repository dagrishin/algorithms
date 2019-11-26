"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

from random import random
N = 10

MASS = [int(random() * 100) for i in range(N)]
print(MASS)
# если пользователь вводит руками массив,
# то сначала я ищу максимальный и ему присваиваю min_1 и min_2
min_1 = 101
min_2 = 101

for i in range(len(MASS)):
    if MASS[i] < min_2:
        min_2 = MASS[i]
        if min_2 < min_1:
            min_1, min_2 = min_2, min_1

print(min_1, min_2)
