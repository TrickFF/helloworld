# Можно объявить пустой список
empty_list = []

# Можно объявить список с элементами
friends = ['Max', 'Leo', 'Kate']

# Тип списка - list
print(type(friends))

# Как и в строк для списка доступны индексы
print('Второй друг - ', friends[1])
print('Первый друг с конца - ', friends[-1])

# Также можно применять срезы
print(friends[1: 2])
print(friends[: 2])
print(friends[1:])

# len(список) - подсчет количества элементов в списке
print(len(friends))

# [имя списка].append('элемент') - добавление элемента в список
friends.append('Ron')
print(friends)

# [имя списка].pop() - удаляем последний элемент и выводим его
# [имя списка].clear() - очищаем весь список
# [имя списка].remove('элемент') - удаление элемента из списка по его значению
friends.remove('Ron')
print(friends)

# del [имя списка][индекс] - удаление элемента из списка по его индексу
del friends[2]
print(friends)

# Списки можно также сортировать, копировать и пр.



