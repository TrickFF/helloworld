# 1. Вывод чисел от 0 до 100
# 2. вывод чисел от 0 до n, где n вводит пользователь
# 3. вывод четных чисел от 0 до n

# 55 мин видео

number = int(input('Введите число от 0 до 100 '))
counter = 0
counter_str = ''

# 1
while counter <= 99:
    counter = counter + 1
    counter_str = counter_str + str(counter)

print(counter_str)

#2
counter = 0
counter_str = ''
while counter <= number-1:
    counter = counter + 1
    counter_str = counter_str + str(counter)

print(counter_str)

#3
counter = 0
counter_str = ''
while counter <= number:
    if counter % 2 == 0 and counter != 0:
        counter_str = counter_str + str(counter)
        counter = counter + 1
    else:
        counter = counter + 1

print(counter_str)