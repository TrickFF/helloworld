ale = 71

age = int(input('Введите свой возраст - '))

# +
after20 = int(age) + 20
print('Через', '20', 'лет Вам будет', after20, 'лет')
# -
alive = ale - age
print('По статистике Вам осталось жить примерно', alive, 'года')

# *
count = 144000000
all_alive = count * ale
print('Среднее время жизни всех людей =', all_alive, 'лет')

# /

live_part = age / ale
print('Часть прожитой жизни', live_part)

# // целая часть от деления

live_part2 = age // ale
print('Часть прожитой жизни', live_part2)

# % Остаток от деления
live_part3 = age % ale
print(age % ale)
print(live_part3)
print(9 % 2)
# % Возведение в степень
print(age ** 2)
