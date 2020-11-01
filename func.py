# модуль числа
print('Модуль -7 =',abs(-7))

#min, max
numbers = [5, 15, 7, 1, -9, 0]
print('Максимальное из [5, 15, 7, 1, -9, 0] - ', max(numbers))
print('Максимальное из [5, 15, 7, 1, -9, 0] - ', min(numbers))

#round
print('10.469461 с округлением до 2х знаков =', round(10.469461, 2))

#sum
print('Сумма чисел [5, 15, 7, 1, -9, 0] =', sum(numbers))

#enumerate
winners = ['leo', 'max', 'kate']
for number, winner in enumerate(winners, 1):
    print(number,' ', winner)
