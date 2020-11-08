# 1: Даны два списка фруктов. Получить список фруктов, присутствующих в обоих исходных списках.
#     Примечание: Списки фруктов создайте вручную в начале файла.

fru1 = ['apple', 'banana', 'kiwi', 'pear']
fru2 = ['banana', 'kiwi', 'tangerine']

fru3 = []
for fru in fru1:
    if fru in fru2:
        fru3.append(fru)

print(fru3)

fru3 = []
fru3 = [fru for fru in fru1 if fru in fru2]
print(fru3)