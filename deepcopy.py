import copy

a = [1, 2, [3, 4]]

b = copy.deepcopy(a)
b[2][1] = 200

# список a не изменился
print(a)
print(b)