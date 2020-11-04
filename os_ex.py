import os

# имя ОС
print(os.name)
# текущая рабочая директория
print(os.getcwd())
# создаем новый путь
new_path = os.path.join(os.getcwd(), 'new_f') # текущий путь + имя новой папки
# создаем папку по новому пути
os.mkdir(new_path)