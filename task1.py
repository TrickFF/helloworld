# 1: Запросите от пользователя число, сохраните в переменную, прибавьте к числу 2 и выведите результат на экран.
# Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.

# ввод числа пользователем
number = int(input('Введите число - '))
print(number + 2)

# 2 Используя цикл, запрашивайте у пользователя число, пока оно не станет больше 0, но меньше 10
# После того, как пользователь введет корректное число, возведите его в степень 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число неверное, и говорите о диапазоне допустимых. И просите ввести заново.
# Допустим, пользователь ввел 2, оно подходит. Возводим его в степень 2 и выводим 4.

#import time
#start = time.perf_counter() - счетчик времени

# вариант 1

# ввод числа пользователем
number = int(input('Введите число от 0 до 10 - '))


while number <= 0 or number >= 10:
    print('Число должно быть больше 0, но меньше 10')
    number = int(input('Введите число от 0 до 10 - '))
else:
    print('Введеное число во 2й степени составит - ', number ** 2)

#print(time.perf_counter() - start, 'var1') - вывод времени выполнения

# Вариант 2

#while True:
#    number = int(input('Введите число от 0 до 10 '))
#    number = 5
#    if number > 0 and number < 10:
#        print('Введеное число во 2й степени составит - ', number**2)
#        break
#    else:
#        print('Число должно быть больше 0, но меньше 10')

#print(time.perf_counter() - start, 'var2') - вывод времени выполнения