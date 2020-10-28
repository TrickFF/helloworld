print('**-----------------Задание1-----------------**')

# 1. Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке.
#    Примечание. Списки создайте вручную, например так:

my_list_1 = [2, 5, 8, 2, 12, 12, 4, 5, 6, 8]
my_list_2 = [2, 7, 12, 3, 3, 7, 11]

# Приводим список 2 ко множеству для получения уникальности элементов
set_list_2 = set(my_list_2)

# переводим полученное множество обратно в список
my_list_3 = list(set_list_2)

for i in my_list_3:
    while i in my_list_1:
        my_list_1.remove(i)

print('Новый список: ', my_list_1)

print('**-----------------Задание2-----------------**')

# 2. Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
#    Ваша задача — вывести дату в текстовом виде, например: второе ноября 2013 года.
#    Склонением пренебречь (2000 года, 2010 года)

# объявляем необходимые списки и словари
d1 = ['десятое', 'двадцать', 'двадцатое', 'тридцать', 'тридцатое']
d2 = ['первое', 'второе', 'третье', 'четвертое', 'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое']
d3 = ['одинадцатое', 'двенадцатое', 'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое', 'семнадцатое',
      'восемнадцатое', 'девятнадцатое']
month = {
    1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 6: 'июня', 7: 'июля',
    8: 'августа', 9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'
}

# Цикл проверки корректности вводимых данных
while True:
    # ввод даты пользователем
    date = input('Введите дату в формате dd.mm.yyyy - ')

    # переводим дату5 из строки в список
    date_list = date.split('.')
    # переводим месяц в число
    mint = int(date_list[1])
    # переводим день в число
    dint = int(date_list[0])
    if mint < 0 or mint > 12 or dint < 0 or dint > 31:
        print('Вы ввели дату неверно!')
        continue
    break

# присваиваем месяцу текстовое значение из справочника
mm = ''
for key, val in month.items():
    if key == mint:
        mm = val

# определяем последнюю цифру числа
last_d_str = date_list[0]
last_d = int(last_d_str[-1])

# присваиваем дню текстовое значение из списков
if dint >= 1 and dint < 10:
    dd = d2[dint - 1]
elif dint == 10:
    dd = d1[0]
elif dint > 10 and dint < 20:
    dd = d3[dint - 11]
elif dint == 20:
    dd = d1[2]
elif dint > 20 and dint < 30:
    dd = d1[1] + ' ' + d2[last_d - 1]
elif dint == 30:
    dd = d1[4]
elif dint == 31:
    dd = d1[3] + ' ' + d2[0]

print('Вы ввели дату - ', dd, mm, date_list[2], 'года')

print('**-----------------Задание3-----------------**')

# 3. Дан список заполненный произвольными целыми числами.
#    Получите новый список, элементами которого будут только уникальные элементы исходного.
#    Примечание. Списки создайте вручную, например так:

my_list_1 = [2, 5, 12, 22, 11, 8, 6, 2, 12, 1, 5, 2, 5, 8, 9, 12, 14, 13, 13, 6, 3, 14, 93, 6, 15, 1]
id_list = set()

# Создаем 2й список из 1го
my_list_2 = my_list_1.copy()

# Сортируем 2й список и определяем его длинну
my_list_2.sort()
ln = len(my_list_2)

# В отсортированном списке выявляем индексы дублирующихся объектов, записываем их в множество id_list
for i in range(ln-1):
    if int(my_list_2[i]) == int(my_list_2[i+1]):
        id_list.add(i)
        id_list.add(i+1)

# Удаляем из списка элементы с выбранными индексами
for id in sorted(id_list, reverse=True):
    del my_list_2[id]

print('Старый список: ', my_list_1)
print('Новый список с уникальными значениями: ', my_list_2)
