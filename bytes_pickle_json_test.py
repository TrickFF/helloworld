import json

tracks = [
    {'name': 'Вечная любовь', 'artist': 'Агата Кристи'},
    {'name': 'Angel', 'artist': 'Massive Attack'},
{'name': 'Jamming', 'artist': 'Bob Marley'}
]

with open('tracks.json', 'w', encoding='utf-8') as f:
    json.dump(tracks, f)

print('Выгрузка окончена')
