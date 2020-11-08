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

if __name__ == '__main__':
    # пользователь выбирает уровень сложности
    lvl = 0
    while lvl < 1 or lvl > 3:
        lvl = int(input('Выберите уровень сложности - 1(easy), 2(medium) или 3(hard) - '))
        if lvl < 1 or lvl > 3:
            print('Вы ввели некорректный уровень сложности, попробуйте еще раз')

def level(lvl):
    print(f'Уровень сложности - {lvl}')
    if lvl == 1:
        count = levels[1]
    elif lvl == 2:
        count = levels[2]
    else:
        count = levels[3]
    return count


if __name__ == '__main__':
    count = level(lvl)

if __name__ == '__main__':
    print(f'У вас {count} попыток')


def guess_the_number(count):
    # пользователь угадывает число
    user_number = None
    trie = count
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
            print(f'Поздравляем, вы угадали число {number} за {trie - count} попыток!')
            exit()
    print(f'К сожалению, вы проиграли, у вас осталось {count} попыток.')
    print(f'Компьютер загадал число {number}')