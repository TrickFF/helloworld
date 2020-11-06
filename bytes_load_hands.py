# читаем объект из файла

# открываем файл
with open('person.dat', 'rb') as f:
    # теперь на м надознать как мы записывали объект
    # прочитаем файл в список
    result = f.readlines()

print(result)

# теперь воссоздаем исходный объект
person = {}
# первый элемент это - имя
person['name'] = result[0].decode('utf-8').replace('\n', '')
# далее идут телефоны
phones = []
for bphones in result[1:]:
    phones.append(bphones.decode('utf-8').replace('\n', ''))

person['phones'] = phones

# получили исходный объект. Это боль
print(person)