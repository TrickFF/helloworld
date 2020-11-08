import os
import shutil
import datetime

# смена текущей директории
def change_dir(name):
    os.chdir(name)
    print(os.getcwd())

# запись информации о работе мнеджера в файл
def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


if __name__ == '__main__':
    save_info('Информация обновлена')


# копирование файлов и папок
def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Такая директория уже существует!')
    else:
        shutil.copy(name, new_name)


if __name__ == '__main__':
    copy_file('test.dat', 'test2.dat')


# удаление файла/папки
def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


if __name__ == '__main__':
    delete_file('text.dat')


# просмотр списка папок и файлов
def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


if __name__ == '__main__':
    get_list()


# функция для создания папки
def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая директория уже существует!')


if __name__ == '__main__':
    create_folder('test_dir')


# функция для создания файла
def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


if __name__ == '__main__':
    create_file('text.dat')
    create_file('text.dat', 'some text')
