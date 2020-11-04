from math import *
from random import randint, randrange

print(pi) # при варианте импорта со * не нужно указывать модуль math при вызове функции
print(sin(30))

print(randint(1, 10)) # при импорте конкретных функций из модуля, название модуля при их вызове можно не указывать

print(mth.factorial(100)) # факториал числа

# факториал числа без math
a = int(input('Введите любое положительное число - '))
b = 1
for i in range(a):
    b = b * (i+1)
print(b)