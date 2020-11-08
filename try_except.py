number = int(input('Введите число - '))
try:
    result = 100 / number
except:
    print('На 0 делить нельзя')
    exit()

print(round(result, 2))