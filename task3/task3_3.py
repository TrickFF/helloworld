# 3: Создайте модуль main.py. Из модулей реализованных в заданиях 1 и 2
# сделайте импорт в main.py всех функций. Вызовите каждую функцию в main.py
# и проверьте что все работает как надо.
# Примечание: Попробуйте импортировать как весь модуль целиком (например из задачи 1),
# так и отдельные функции из модуля.

import sys
from task3_1 import create_folder
from task3_1_2 import del_folder
import task3_2

arg =sys.argv[1]

if arg == 'create':
    create_folder()
elif arg == 'del':
    del_folder()
elif arg == 'rnd':
    print(task3_2.get_random([1, 4, 6, 9, 12]))

