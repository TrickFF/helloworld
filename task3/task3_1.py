# 1: Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py).
# В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой
# запущен данный код. Затем создайте вторую функцию удаляющую эти папки. Проверьте
# работу функций в этом же модуле.

import os

def create_folder():
    for i in range(1, 10):
        os.mkdir('dir_' + str(i))

if __name__=='__main__':
    create_folder()
