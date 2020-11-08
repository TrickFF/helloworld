try:
    number = number = int(input('Введите число - '))
except ValueError:
    print('Ошибка значения. Введено не число')
    exit()

try:
    result = 100 / number
except ZeroDivisionError:
    print('На 0 делить нельзя')
    exit()
except Exception:
    print('Неизвестная ошибка')
    exit()

print(round(result, 2))