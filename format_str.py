# Форматирование строк:

name = 'Leo'
age = 30

# 1. Конкатенация (не рекомендуется) - прибавление через +
hello_str = 'Привет, ' + name + ', тебе ' + str(age) + ' лет!'
print(hello_str)

# 2. %
hello_str = 'Привет, %s, тебе %d лет!' % (name, age)  # %s - строка, #d - число
print(hello_str)

# 3. Функция format(рекомендуется)
hello_str = 'Привет, {}, тебе {} лет!'.format(name, age)
print(hello_str)
