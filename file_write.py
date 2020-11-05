# открываем файл на запись
f = open('first.txt', 'w')
f.write('Hello\n')
f.write('World!\n')

f.writelines(['Hello\n', 'Python\n'])
