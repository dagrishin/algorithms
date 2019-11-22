"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from random import random
N = 10

MASS = [int(random() * 100) for i in range(N)]
print(MASS)
MAX_INDEX = 0
MIN_INDEX = 0
MAX = MASS[0]
MIN = MASS[0]
for i in range(1, len(MASS)):
    if MASS[i] > MAX:
        MAX = MASS[i]
        MAX_INDEX = i
    if MASS[i] < MIN:
        MIN = MASS[i]
        MIN_INDEX = i
S = 0
print(MAX_INDEX, MIN_INDEX)
if MAX_INDEX > MIN_INDEX:
    for i in range(MIN_INDEX + 1, MAX_INDEX):
        S += MASS[i]
if MAX_INDEX < MIN_INDEX:
    for i in range(MAX_INDEX + 1, MIN_INDEX):
        S += MASS[i]

print(S)
