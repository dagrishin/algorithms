# 5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.
from random import random
N = 20
LEFT = -10
RIGHT = 10

MASS = [int(random() * (RIGHT - LEFT + 1)) + LEFT for i in range(N)]
print(MASS)
MIN_MAX = LEFT - 1
MIN_MAX_INDEX = None


for i in range(len(MASS)):
    if MIN_MAX < MASS[i] < 0:
        MIN_MAX = MASS[i]
        MIN_MAX_INDEX = i
print(f'{MIN_MAX} : {MIN_MAX_INDEX}' if MIN_MAX != LEFT - 1 else 'нет отрицательных чисел' )

