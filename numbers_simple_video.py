# 1. Вывод чисел от 0 до 100
# 2. вывод чисел от 0 до n, где n вводит пользователь
# 3. вывод четных чисел от 0 до n


number = 0
n = int(input('Введите число - '))

# 1

while number <= 100:
    print(number)
    number += 1

#2
number = 0
while number <= n:
    print(number)
    number += 1

#2
number = 0
while number <= n:
    if number % 2 == 0:
        print(number)
    number += 1