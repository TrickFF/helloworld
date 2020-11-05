# открываем файл на чтение
f = open('first.txt', 'r')

for line in f:
    print(line.replace('\n', ''))

# 1й вариант
f.close()

# 2й вариант
with open ('first.txt', 'r') as f:
    for line in f:
        print(line.replace('\n', ''))

print('end')