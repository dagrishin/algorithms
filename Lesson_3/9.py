# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.


from random import random
n = 5
M = [[int(random() * 10) for i in range(n)] for j in range(n)]
print(M)
max_el = None
for i in range(n):
    min_el = M[i][0]
    for j in range(1, n):
        if M[i][j] < min_el:
            min_el = M[i][j]
    if max_el == None or min_el > max_el:
        max_el = min_el
print(max_el)
