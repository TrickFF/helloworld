# 3. Напишите функцию которая принимает на вход список. Функция создает из этого
# списка новый список из квадратных корней чисел (если число положительное)
# и самих чисел (если число отрицательное) и возвращает результат
# (желательно применить генератор и тернарный оператор при необходимости).
# В результате работы функции исходный список не должен измениться.
# Например:
# old_list = [1, -3, 4]
# result = [1, -3, 2]
#
#     Примечание: Список с целыми числами создайте вручную в начале файла.
#     Не забудьте включить туда отрицательные числа. 10-20 чисел в списке
#     вполне достаточно.

old_list = [1, -1, 2, 2, 4, 5, 6, 7, 8, 9]

# плохой пример
# def new_sqrt_list(input_list):
#     input_list = input_list[:]
#     for i in range(len(input_list)):
#         number = input_list[i]
#         if number > 0:
#             input_list[i] = number**0.5
#     return input_list
#
# result = new_sqrt_list(old_list)
# print(result)
# print(old_list)

print()

# хороший пример с генератором
def new_sqrt_list2(input_list):
    result = [number**0.5 if number > 0 else number for number in input_list]
    return result

result = new_sqrt_list2(old_list)
print(result)
print(old_list)