# 3:
import random

player = {
    'name': '',
    'health': 100,
    'min_damage': 30,
    'max_damage': 50,
    'armor': 1.2
}

enemy = {
    'name': 'COVID-19',
    'health': 100,
    'min_damage': 10,
    'max_damage': 50
}

player['name'] = input('Введите свое имя - ')


def attack(player, enemy):
    dmg_player = random.randint(player['min_damage'], player['max_damage'])
    dmg_enemy = random.randint(enemy['min_damage'], enemy['max_damage'])
    player['health'] -= int(dmg_enemy/player['armor'])
    enemy['health'] -= dmg_player
    return f"{enemy['name']} нанес {dmg_enemy} урона. Получено {int(dmg_enemy/player['armor'])} урона с учетом брони." \
           f" Здоровье игрока после атаки - {player['health']}. \n" \
           f"{player['name']} нанес {dmg_player} урона. Здоровье врага после атаки - {enemy['health']}."


print(attack(player, enemy))