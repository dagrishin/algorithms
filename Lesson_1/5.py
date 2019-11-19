#5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.

p = 96
letter1 = input('letter1')
letter2 = input('letter2')
print('letter1:', ord(letter1)-p)
print('letter2:', ord(letter2)-p)
print('letters:', ord(letter2) - ord(letter1) -1 if ord(letter2) >= ord(letter1) else (ord(letter1) - ord(letter2) -1))