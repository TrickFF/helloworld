number = 0
n = int (input('Введите n - '))

while number <= n:
    if number % 2 == 0:
        number += 1
        continue
    print(number)
    number += 1