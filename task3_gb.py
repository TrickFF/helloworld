#4: +-
import random

# создаем словари
player = {
    'name': '',
    'health': 100,
    'damage': 50,
    'armor': 1.5
}

enemy = {
    'name': 'COVID-19',
    'health': 100,
    'damage': 20,
    'armor': 1
}
# игрок вводит свое имя
player['name'] = input('Введите свое имя - ')


def get_damage(damage, armor):
    return damage / armor

def attack(unit, target):
    damage = get_damage(unit['damage'], target['armor'])
    target['health'] -= damage

attack(player, enemy)
print(enemy)
attack(enemy, player)
print(player)


exit()

# 3: +-

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

# 2. OK
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

# 1: OK
def data(name, age, city):
    return f'{name}, {age} год(а), проживает в городе {city}'

# вводим исходные данные
name = input(f'Введите имя - ')
age = int(input(f'Введите возраст - '))
city = input(f'Введите город - ')

print(data(name, age, city))