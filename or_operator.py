import math

if 2 > 1 or math.sqrt(-1):
    print('Ошибки не будет, т.к. 1е условие истина')

# Возвращает первую истину
print(0 or [] or 8 or 1)

# Возвращает последнюю ложь
print(0 or [] or () or {})
