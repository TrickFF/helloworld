import sys

from core import save_info, copy_file, delete_file, get_list, create_folder, create_file, change_dir
from game1 import level, guess_the_number

try:
    command = sys.argv[1]
except IndexError:
    print('Введите команду (help для справки)')
    exit()

if command == 'list':
    if len(sys.argv) > 2:
        get_list(True)
        exit()
    get_list()
    save_info('Выведен список файлов/папок')
elif command == 'create_file':
    try:
        name = sys.argv[2]
    except NameError:
        print('Введите название файла')
        exit()
    except IndexError:
        print('Введите название файла')
        exit()
    create_file(name)
    print(f'Файл {name} создан')
    save_info(f'Файл {name} создан')
elif command == 'cd':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Введите название директории')
        exit()
    change_dir(name)
    print(f'Перешли в директорию {name}')
    save_info(f'Перешли в директорию {name}')
elif command == 'create_folder':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Введите название директории')
        exit()
    create_folder(name)
    print(f'Директоия {name} создана')
    save_info(f'Директоия {name} создана')
elif command == 'delete':
    try:
        name = sys.argv[2]
    except IndexError:
        print('Введите название файла/директории')
        exit()
    try:
        delete_file(name)
    except FileNotFoundError:
        print('Такого файла/директории не существует')
        exit()
    print(f'Файл/директоия {name} удален/а')
    save_info(f'Файл/директоия {name} удален/а')
elif command == 'copy':
    try:
        name = sys.argv[2]
        new_name = sys.argv[3]
    except IndexError:
        print('Введите название исходного файла/директории и нового названия через пробел')
        exit()
    try:
        copy_file(name, new_name)
    except FileNotFoundError:
        print('Такого файла/директории не существует')
        exit()
    print(f'Файл/директоия {name} скопирован/а с именем {new_name}')
    save_info(f'Файл/директоия {name} скопирован/а с именем {new_name}')
elif command == 'help':
    print(f'Команды менеджера:\n'
          f'list [любой параметр через пробел] - вывод списка файлов/папок текущей директории \n'
          f'create_file name - создание файла \n'
          f'create_folder name - создание директории \n'
          f'delete name - удаление директории/файла \n'
          f'copy name1 name2 - копирование директории/файла \n'
          f'game - сыграть в игру')
    save_info(f'Выведен список команд')
elif command == 'game':
    save_info(f'Запущена игра')
    lvl = 0
    while lvl < 1 or lvl > 3:
        lvl = int(input('Выберите уровень сложности - 1(easy), 2(medium) или 3(hard) - '))
        if lvl < 1 or lvl > 3:
            print('Вы ввели некорректный уровень сложности, попробуйте еще раз')
    count = level(lvl)
    print(f'У вас {count} попыток')
    guess_the_number(count)