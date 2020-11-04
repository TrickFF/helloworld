# 2: Создайте модуль. В нем создайте функцию, которая принимает список
# и возвращает из него случайный элемент. Если список пустой функция должна
# вернуть None. Проверьте работу функций в этом же модуле.
#    Примечание: Список для проверки введите вручную. Или возьмите этот: [1, 2, 3, 4]

import random

list = ['2', '5', 'h1', 'r3', 'test', 'one']

def get_random(input_list):
    if input_list:
        result = random.choice(input_list)
        return result

if __name__=='__main__':
    print(get_random(list))
    print(get_random([]))