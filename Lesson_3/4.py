# 4.	Определить, какое число в массиве встречается чаще всего.

from random import random
N = 10

MASS = [int(random()*4) for i in range(N)]
print(MASS)
SUM = 1
SUM_INDEX = 0
for i in range(len(MASS)):
    s = 1
    for j in range(i + 1, len(MASS)):
        if MASS[i] == MASS[j] and i != j:
            s += 1
    if s > SUM:
        SUM = s
        SUM_INDEX = i

print(MASS[SUM_INDEX])
print(SUM)
