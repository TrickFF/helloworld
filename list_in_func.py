numbers = [1, 2, 3]

def change_bumber_in_list(input_list):
    input_list[1] = 200

# после вызова функции
change_bumber_in_list(numbers)
# список в основной программе тоже изментися
print(numbers)

