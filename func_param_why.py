def my_filter(numbers, function):
    result = []
    for number in numbers:
        if function(number):
            result.append(number)
    return result


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

def is_even(number):
    return number % 2 == 0

# вывод четных чисел
print(my_filter(numbers, is_even))
# тоже самое через lambda функцию без создания доп. функции is_even
print('lambda -',my_filter(numbers, lambda number: number % 2 == 0))

# если нужны нечетные числа
def is_not_even(number):
    return number % 2 != 0

print(my_filter(numbers, is_not_even))
# тоже самое через lambda функцию без создания доп. функции is_not_even
print('lambda -',my_filter(numbers, lambda number: number % 2 != 0))

# если нужны числа > 4
def more_than_four(number):
    return number > 4

print(my_filter(numbers, more_than_four))
# тоже самое через lambda функцию без создания доп. функции more_than_four
print('lambda -',my_filter(numbers, lambda number: number > 4))
