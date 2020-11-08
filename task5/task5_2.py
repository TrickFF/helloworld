# 2: Дан список, заполненный произвольными числами. Получить список из элементов
# исходного, удовлетворяющих следующим условиям:
# Элемент кратен 3,
# Элемент положительный,
# Элемент не кратен 4.
#
# Примечание: Список с целыми числами создайте вручную в начале файла.
# Не забудьте включить туда отрицательные числа. 10-20 чисел в списке вполне достаточно.

numbers = [1, 5, -9, 10, 27, 8, 17, 45, 100, 11, -7, 12, -27]

result = [number for number in numbers if number > 0 and number % 3 == 0 and number % 4 != 0]
print(result)