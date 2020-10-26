friend = {
    'name': 'Max',
    'age': 23,
    'has_car': True
}

# по ключам
for key in friend.keys():
    print(key)
    print(friend[key])
# или так
for key in friend:
    print(key)
    print(friend[key])

# По значаниям
for val in friend.values():
    print(val)
# или так
for val in friend:
    print(val)

# по паре ключ, значение. Перебор пары в виде картежа(!)
for item in friend.items():
    print(item)
# или так
for key, val in friend.items():
    print(key)
    print(val)