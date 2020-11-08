# добавление элемента в список

# классический способ
def add_to_list(imput_list=None):
    if imput_list is None:
        imput_list = []
    imput_list.append(2)
    return imput_list

result = add_to_list([0, 1])
print(result)
result = add_to_list()
print(result)

# тоже самое через or
def add_to_list(input_list=None):
    # используем свойство or вместо условия
    input_list = input_list or []
    input_list.append(2)
    return input_list
result = add_to_list([0, 1])
print(result)
result = add_to_list()
print(result)
