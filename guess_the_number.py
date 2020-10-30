# Пользователь угадывает число, загаданное компьютером

import random

# уровни сложности
levels = {
    1: 10,
    2: 6,
    3: 4
}

# загадываем число
number = random.randint(1, 100)

# пользователь выбирает уровень сложности
lvl = 0
while lvl < 1 or lvl > 3:
    lvl = int(input('Выберите уровень сложности - 1(easy), 2(medium) или 3(hard) - '))
    if lvl < 1 or lvl > 3:
        print('Вы ввели некорректный уровень сложности, попробуйте еще раз')

if lvl == 1:
    count = levels[1]
elif lvl == 2:
    count = levels[2]
else:
    count = levels[3]

print(f'У вас {count} попыток')

# пользователь угадывает число
user_number = None
while user_number != number and count > 0:
    # пользователь вводит число
    user_number = int(input('Попробуйте угадать число от 1 до 100 - '))
    count -= 1
    if user_number > number:
        print('Введеное число больше загаданного, попробуйте еще раз!')
        print(f'Осталось попыток - {count}')
        continue
    elif user_number < number:
        print('Введеное число меньше загаданного, попробуйте еще раз!')
        print(f'Осталось попыток - {count}')
        continue
    else:
        print(f'Поздравляем, вы угадали число {number} за {levels[lvl] - count} попыток!')
        exit()

print(f'К сожалению, вы проиграли, у вас осталось {count} попыток.')
print(f'Компьютер загадал число {number}')
