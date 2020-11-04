# 1: Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
# Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»
def data(name, age, city):
    return f'{name}, {age} год(а), проживает в городе {city}'

# вводим исходные данные
name = input(f'Введите имя - ')
age = int(input(f'Введите возраст - '))
city = input(f'Введите город - ')

print(data(name, age, city))

# 2. Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.
numbers = []

# функция, вычисляющая максимум
def max_number():
    return max(numbers)

# ввод пользователем чисел
for i in range(3):
    number = int(input(f'Введите {i + 1}е число - '))
    numbers.append(number)

print(f'Максимальное из введеных чисел - {max_number()}')

# Тоже самое через lambda функцию
print('Максимальное из введеных чисел -', max(numbers, key=lambda number: int(number)))

# 3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50.
# ### Поэкспериментируйте с значениями урона и жизней по желанию.
# ### Теперь надо создать функцию attack(person1, person2). Примечание: имена аргументов можете указать свои.
# ### Функция в качестве аргумента будет принимать атакующего и атакуемого.
# ### В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения.

import random

# создаем словари
player = {
    'name': '',
    'health': 100,
    'min_damage': 30,
    'max_damage': 50
}

enemy = {
    'name': 'COVID-19',
    'health': 100,
    'min_damage': 10,
    'max_damage': 50
}
# игрок вводит свое имя
player['name'] = input('Введите свое имя - ')

# функция расчета урона
def attack(player, enemy):
    # расчитываем урон, как случайное число между минимальным и максимальным воможными значениями урона
    dmg_player = random.randint(player['min_damage'], player['max_damage'])
    dmg_enemy = random.randint(enemy['min_damage'], enemy['max_damage'])
    player['health'] -= dmg_enemy
    enemy['health'] -= dmg_player
    return f"{enemy['name']} нанес {dmg_enemy} урона. Здоровье игрока после атаки - {player['health']}. \n" \
           f"{player['name']} нанес {dmg_player} урона. Здоровье врага после атаки - {enemy['health']}."

print(attack(player, enemy))
