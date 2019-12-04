"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""
from memory_profiler import profile

number = '1234564646465327293707543673765256325674385463757575129870'

@profile
def revers_rec(number):
    if len(number) == 1:
        return number
    return str(int(number) % 10) + revers_rec(str(int(number) // 10))

@profile
def revers_cycl(number):
    result = ''
    for s in number:
        result = f'{s}{result}'
    return result

@profile
def test_fun():
    from random import random
    from sys import getsizeof
    sum_memory = 0
    n = 500
    sum_memory += getsizeof(n)
    M = [[int(random() * 10) for i in range(n)] for j in range(n)]
    sum_memory += getsizeof(M)
    print(M)
    max_el = None
    for i in range(n):
        min_el = M[i][0]
        for j in range(1, n):
            if M[i][j] < min_el:
                min_el = M[i][j]
        if max_el == None or min_el > max_el:
            max_el = min_el
    sum_memory += getsizeof(min_el) + getsizeof(max_el)
    print('memory =', sum_memory)
    return max_el

print(revers_rec(number))
print(revers_cycl(number))
print(test_fun())

""" os windows 10 x64, python 3.6
профилирование очень замедляет выполнение программы, 
не показывает сколько памяти занято даже там где точно память была использована,
т.к. единици измерения памяти в Mib, поэтому использовал getsizeof() 
"""