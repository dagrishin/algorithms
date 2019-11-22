"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""
from random import random
n = 5
M = [[] for i in range(n)]
print(M)
for i in range(n):
    line = []
    s = 0
    for j in range(n - 1):
        el = int(random() * 10)
        M[i].append(el)
        s += el
    M[i].append(s)
print(M)
for i in range(n):
    for j in range(n):
        print(M[i][j], end=' ')
    print()
