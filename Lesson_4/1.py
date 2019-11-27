"""
Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""
import timeit

number = '1234564646465327293707543673765256325674385463757575129870'


def revers_rec(number):
    if len(number) == 1:
        return number
    return str(int(number) % 10) + revers_rec(str(int(number) // 10))


def revers_cycl(number):
    result = ''
    for s in number:
        result = f'{s}{result}'
    return result


def rev(number):
    return number[::-1]


print(
    timeit.timeit(
        "revers_rec(number)",
        setup="from __main__ import revers_rec, number", number=1000))

print(
    timeit.timeit(
        "revers_cycl(number)",
        setup="from __main__ import revers_cycl, number", number=1000))

print(
    timeit.timeit(
        "rev(number)",
        setup="from __main__ import rev, number",
        number=1000))

"""
0.13821
0.01034560000000001
0.00048270000000000257
Самая медленная рекурсия а срез оказался самым быстрым, очень очень быстрым
"""