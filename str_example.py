# Выбраь Топ3 из Топ5 на соревнованиях
top5 = 'Первые 5 мест на соревнованиях: 1. иванов, 2. петров, 3. сидоров, 4. орлов, соколов.'

start = top5.find('1')
end = top5.find('4')
top3 = top5[start: end-2]

result = 'Поздравляем {} c успехом!'.format(top3.upper())
print(result)
