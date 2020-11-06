import json

friends = [
    {'name': 'Max', 'age': 23, 'phones': [123, 547]},
    {'name': 'Leo', 'age': 33}
]

# тип объекта
print(friends)
print(type(friends))

# преобразуем список друзей в json
json_friends = json.dumps(friends)

# выводим что получилось
print(json_friends)
print(type(json_friends))

# обратно из json в объект
friends = json.loads(json_friends)
print(friends)
print(type(friends))