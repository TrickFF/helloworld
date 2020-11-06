import json

friends = [
    {'name': 'Max', 'age': 23, 'phones': [123, 547]},
    {'name': 'Leo', 'age': 33}
]

print(type(friends))

with open('friends.json', 'w') as f:
    # преобразуем список друзей в json
    json_friends = json.dump(friends, f)

with open('friends.json', 'r') as f:
    # обратно из json в объект
    friends = json.load(f)


print(friends)
print(type(friends))