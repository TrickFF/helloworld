# в зависимости от параметра вызывать определенную функцию скрипта
# параметр ping -> функция выводит pong
# 2 параметра name и [Имя] -> функция приветствия пользователя
# параметр list - показать содержимое текущей директории

import sys, os

def ping():
    print('Pong')

def hello(name):
    print('Hello', name)

def get_info():
    for i in os.listdir():
        print(i)

command = sys.argv[1]

if command == 'ping':
    ping()
elif command == 'list':
    get_info()
elif command == 'name':
    name = sys.argv[2]
    hello(name)