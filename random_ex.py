from random import randint, choice, sample, shuffle

# 1 загадать случайное число от 0 до 100
print(randint(0, 100))
# 2 выбрать победителя лотереи из списка players
players = ['Max', 'Leo', 'Kate', 'Ron', 'Bill']

print(choice(players))
# 3 Выбрать 3х победителей лотереи
print(sample(players, 3))
# 4 перемешать карты в списке cards
cards = ['6', '7', '8', '9', '6', '7', '8', '9', 'T', 'J', 'K', 'A']
print(cards)
shuffle(cards)
print(cards)