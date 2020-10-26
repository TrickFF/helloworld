friend_name = 'Max'
friends = ['Max', 'Leo', 'Kate']
roles = ('admin', 'guest', 'user')

if 'Max' in friends:
    print('У меня есть этот друг')

if 'M' in friend_name:
    print('Буква M есть в имени друга')

i = 0
friend = ''
while i < len(friends):
    friend = friends[i]
    print(friend)
    i += 1

# For
for friend in friends:
    print(friend)

for letter in friend_name:
    print(letter)

for role in roles:
    print(role)
