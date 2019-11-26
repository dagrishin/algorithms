#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

from random import random
N = 10

MASS = [int(random()*100) for i in range(N)]
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
MASS[MAX_INDEX], MASS[MIN_INDEX] = MASS[MIN_INDEX], MASS[MAX_INDEX]
print(MASS)
