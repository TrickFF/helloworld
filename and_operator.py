import math

if 1 > 2 and math.sqrt(-1):
    print('Ошибки не будет, т.к. 1е условие ложь')
print('Двигаемся дальше')

# if math.sqrt(-1) and 1 > 2:
#     print('Если поменять местами, то будет ошибка')

# первая ложь
print([1] and [] and '' and 1)

# последняя истина
print([1] and 1 and 20 and 1.1)