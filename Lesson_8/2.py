"""
2*. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""

import hashlib

print(hashlib.sha1('aaa'.encode('utf-8')).hexdigest())

s = 'papa'
arr_hex = []
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        if len(s) != len(s[i:j]):
            h = hashlib.sha1(s[i:j].encode('utf-8')).hexdigest()
            if h not in arr_hex:
                arr_hex.append(h)

print(f'У строки "{s}" {len(arr_hex)} подстрок')
