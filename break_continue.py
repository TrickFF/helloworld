# break
name = None

while True:
    name = input('Кто основатель Python? ')
    if name == 'Гвидо':
        break
    print('Неверно!')

print('Верно!')

# break 2
for i in 'hello world':
    if i == 'o':
        break
    print(i * 2, end='')

# Перенос строки
print('\n')

# continue
number = 0
n = int(input('Введите n - '))

while number <= n:
    if number % 2 == 0:
        number += 1
        continue
    print(number)
    number += 1

# continue 2
for i in 'hello world':
    if i == 'o':
        continue
    print(i * 2, end='')
