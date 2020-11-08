import math

# есть список чисел
numbers = [4, 1, 2, 3, -4, -2, 7, 16]

# нужно создать список из тех чисел, котоорые имеют квадратный корень меньше 2

result = []
# обычный способ
for number in numbers:
    if number > 0:
        sqrt = math.sqrt(number)
        # квадратный корень меньше 2
        if sqrt < 2:
            result.append(number)

print(result)

result = []
# тоже самое через ленивый and
for number in numbers:
    if number > 0 and math.sqrt(number) < 2:
        result.append(number)
print(result)

# черег генератор
result = [number for number in numbers if number > 0 and math.sqrt(number) < 2]
print(result)
