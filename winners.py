#Прорамма должна выводить 3 первых места победителей из указанного пользователем количества участников

uchcount = int(input('Введите количество участников соревнований - '))


list = []
sortlist = []

for a in range(1, uchcount+1):
    list.append(input('Кто занял {} место? - '.format(a)))
    a += 1

sortlist = sorted(list)
print('В соревнованиях приняли участие: {}'.format(sortlist))
print('Поздравляем троих призеров! {} Так держать!'.format(list[0:3]))

