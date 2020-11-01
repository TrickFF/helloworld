#пользователь  вводит 3 числа. Найти min max и sum

numbers = []
a = None
# пользователь вводит 3 числа
for i in range(3):
    number = int(input(f'Введите {i+1}е число - '))
    numbers.append(number)


print(f'Минимальное из введеных чисел - {min(numbers)}, максимальное - {max(numbers)},'
      f' сумма всех чисел составляет - {sum(numbers)}')