import time


def cycle(numb):
    j = 0
    i = 1
    while j != numb and i <= n:
        i += 1
        k = 2
        while k <= i**0.5:
            if i % k == 0:
                break
            k += 1
        if k > i**0.5:
            j += 1

    if i > n:
        return 'Error'
    else:
        return i


def eratosthenes(n, mass, numb):
    i = 2
    if n < numb:
        return 'Error'
    while i * i <= n:
        j = i * i
        while j <= n:
            mass[j - 2] = False
            j += i
        i += 1
    k = 0
    for i in range(n):
        if mass[i]:
            k += 1
            if k == numb:
                return i + 2


n = int(input('N: '))
numb = int(input('Номер i-го простого числа:'))
mass = [True for i in range(n - 1)]

start = time.time()
print('простое число', cycle(numb))
print('время выполнеия', time.time() - start)

start = time.time()
print('простое число', eratosthenes(n, mass, numb))
print('время выполнеия', time.time() - start)

"""
чем ближе i-тое простое число к n тем более выигрышным становиться алгоритм Эратосфена, но если мы берем вычисление простых чисел до n то ему вообще нет равных 
"""