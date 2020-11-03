#4: Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр
# - armor = 1.2 (величина брони персонажа)
#Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон
# по формуле damage / armor
#Следовательно, у вас должно быть 2 функции:
#Наносит урон. Это улучшенная версия функции из задачи 3.
#Вычисляет урон по отношению к броне.

#Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона
# и вычитания его из здоровья персонажа.
import random

# создаем словари
player = {
    'name': '',
    'health': 100.00,
    'min_damage': 20,
    'max_damage': 50,
    'armor': 1.3
}

enemy = {
    'name': 'COVID-19',
    'health': 100.00,
    'min_damage': 10,
    'max_damage': 50,
    'armor': 1.1
}
# игрок вводит свое имя
player['name'] = input('Введите свое имя - ')


# функция атаки с расчетом урона в зависимости от показателя брони
def attack(player, enemy):
    # функция расчета урона
    def damage(player, enemy):
        # расчитываем урон, как случайное число между минимальным и максимальным воможными значениями урона
        dmg_player = random.randint(player['min_damage'], player['max_damage'])
        dmg_enemy = random.randint(enemy['min_damage'], enemy['max_damage'])
        return dmg_player, dmg_enemy

    # импоритиуем значения урона из внутренней функции
    dmg_player, dmg_enemy = damage(player, enemy)
    # расчитываем урон с учетом брони
    player['health'] -= dmg_enemy / player['armor']
    enemy['health'] -= dmg_player / enemy['armor']
    return f"{enemy['name']} нанес {dmg_enemy} урона. Получено {round(dmg_enemy / player['armor'], 2)}" \
           f" урона с учетом брони. Здоровье игрока после атаки - {round(player['health'], 2)}. \n" \
           f"{player['name']} нанес {dmg_player} урона. Получено {round(dmg_player / enemy['armor'], 2)}" \
           f" урона с учетом брони. Здоровье врага после атаки - {round(enemy['health'], 2)}."


print(attack(player, enemy))
