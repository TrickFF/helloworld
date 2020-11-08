try:
    number = number = int(input('Введите число - '))
except ValueError as e:
    print('Ошибка значения. Введено не число')
    print('Информация об ощибке', e)
    exit()

try:
    result = 100 / number
except ZeroDivisionError as e:
    print('На 0 делить нельзя')
    print('Информация об ощибке', e)
    exit()
except Exception as e:
    print('Неизвестная ошибка')
    print('Информация об ощибке', e)
    exit()

print(round(result, 2))