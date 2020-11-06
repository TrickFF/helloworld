person = {'name': 'Max', 'phones': [123, 234]}

# откроем файл
with open('person.dat', 'wb') as f:
    # например запишем объект в файл построчно
    # сначалавозьмем имя
    name = person['name']
    # добавим перенос строки и переведем в байты
    f.write(f'{name}\n'.encode('utf-8'))
    # получим телефоны
    phones = person['phones']
    # запишем каждый телевон в новую строку
    for phone in phones:
        f.write((f'{phone}\n'.encode('utf-8')))

print('Объект записан')

