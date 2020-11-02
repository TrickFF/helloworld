# 3:
import random

player = {
    'name': '',
    'health': 100.00,
    'min_damage': 25.00,
    'max_damage': 50.00,
    'armor': 1.2
}

enemy = {
    'name': 'COVID-19',
    'health': 100.00,
    'min_damage': 1.00,
    'max_damage': 20.00,
    'armor': 0.9
}
# игрок вводит свое имя
player['name'] = input('Введите свое имя - ')

def attack(player, enemy):
    # расчитываем урон, как случайное число между минимальным и максимальным воможными значениями урона
    dmg_player = random.uniform(player['min_damage'], player['max_damage'])
    dmg_enemy = random.uniform(enemy['min_damage'], enemy['max_damage'])
    return dmg_player, dmg_enemy

def damage_reducion(player, enemy):
    a = attack(player, enemy)[1]/player['armor']
    player['health'] -= a
    b = attack(player, enemy)[0]/enemy['armor']
    enemy['health'] -= b
    return f"{enemy['name']} нанес {round(attack(player, enemy)[1], 2)} урона. Получено" \
           f" {round(a, 2)} урона с учетом брони." \
           f" Здоровье игрока после атаки - {player['health']}. \n" \
           f"{player['name']} нанес {round(attack(player, enemy)[0], 2)} урона. Получено " \
           f"{round(b, 2)} урона с учетом брони." \
           f"Здоровье врага после атаки - {enemy['health']}."


#print(attack(player, enemy)[1], attack(player, enemy)[0])
print(attack(player, enemy))
print(f"броня - {player['armor']} - {attack(player, enemy)[1]/player['armor']}")
print(f"броня - {enemy['armor']} - {attack(player, enemy)[0]/enemy['armor']}")
