# Пользователь угадывает число, загаданное компьютером

import random

# уровни сложности
levels = {
    1: 10,
    2: 6,
    3: 4
}

# ПК загадыват число
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

# пользователь выбирает количество игроков
players = 0
while players < 1 or players > 3:
    players = int(input('Введите количество участников от 1 до 3 - '))
    if players < 1 or players > 3:
        print('Вы ввели некорректный количество игроков, попробуйте еще раз')

print(f'Количество игроков - {players}')

# Ввод и сохранение имен игроков
player_names = []
for i in range(players):
    name = input(f'Введите имя {i + 1}го игрока - ')
    player_names.append(name)

# игроки угадывают число
user_number = None
while user_number != number and count >= 0:
    count -= 1
    for i in range(players):
        # пользователь вводит число
        print(f'Ходит игрок {player_names[i]}')
        user_number = int(input('Попробуйте угадать число от 1 до 100 - '))
        if user_number > number:
            print('Введеное число больше загаданного, попробуйте еще раз!')
            continue
        elif user_number < number:
            print(f'{player_names[i]}, введеное число меньше загаданного!')
            continue
        else:
            print(f'Поздравляем, {player_names[i]}, вы угадали число {number} за {levels[lvl] - count} попыток!')
            exit()
    print(f'Осталось попыток - {count}')

print(f'К сожалению, все участники проиграли у вас осталось {count} попыток.')
print(f'Компьютер загадал число {number}')
