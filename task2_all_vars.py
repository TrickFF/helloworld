my_list_1 = [1, 1, 1, 2, 5, 8, 2, 12, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]

# 1.1 Решение 1й задачи

for number in my_list_1[:]:  # без указания [:] пропускает второе и третье число 12
    if number in my_list_2:
        my_list_1.remove(number)
print(my_list_1)
# Ответ: [1, 1, 1, 5, 8, 4]


# 1.2 Решение 1й задачи

for number in my_list_1:
    if number in my_list_2:
        del my_list_1[number]
print(my_list_1)
# Ответ: [1, 1, 1, 5, 8, 4]


# 1.3 Решение 1й задачи
uni_list = []

for number in my_list_1:
    if number not in my_list_2:
        uni_list.append(number)
print(uni_list)
# Ответ: [1, 1, 1, 5, 8, 4]


# 1.4 Решение 1й задачи через множества, выводим уникальные значения

unique_set = set(my_list_1).difference(my_list_2)
unique_list = list(unique_set)
print(unique_list)
# Ответ: [8, 1, 4, 5]


# 2.1 Решение 2й задачи через создание функции

days = {1: "первое",        # создаем словари с данными или базы данных
        2: "второе",        # из которых будем брать данные в функции
        3: "третье"}

months = {1: "января",
          2: "февраля",
          3: "марта"}


def curr_day(day, month, year):     # создаем функцию которая принимает ключи из
    if day in days:                 # созданных выше баз данных и списков и
        day = days[day]             # выводит нам значения ключей
        if month in months:
            month = months[month]
            return f'Сегодня {day} {month} {year} года'

curr_day(1, 1, 2019)
# Ответ: Сегодня первое января 2019 года


my_list_1 = [2, 2, 5, 12, 8, 2, 12]

# 3.1 Решение 3й задачи
uni_list = []
for num in my_list_1:
    if my_list_1.count(num) == 1:
        uni_list.append(num)
print(uni_list)
# Ответ: [5, 8]


# 3.2 Решение 3й задачи
uni_list = []
dupl_list = []
for uni_num in my_list_1:
    if uni_num not in uni_list:
        uni_list.append(uni_num)
    elif uni_num in uni_list:
        dupl_list.append(uni_num)
    if uni_num in dupl_list:
        uni_list.remove(uni_num)
print(uni_list)
# Ответ: [5, 8]

# 3.3 Решение 3й задачи через множества, выводим уникальные значения

uni_set = set(my_list_1)
print(list(uni_set))

# Ответ: [8, 2, 12, 5]