import pickle

person = {'name': 'Max', 'phones': [123, 234], 'age': 20}

# откроем файл
with open('person.dat', 'wb') as f:
    # сразу пишем объект целиком с помощью pickle
    pickle.dump(person, f)

print('Объект записан')

# открываем файл в режиме чтения байтов
with open('person.dat', 'rb') as f:
    # читаем строку байт
    result = f.read()
    print(result)
    print(type(result))
