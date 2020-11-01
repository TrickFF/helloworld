global_var = 1

def my_f():
    # локальная переменная
    local_var = 100
    # мы можем использовать локальную переменную внутри функции
    print('local in local', local_var)
    # глобальная переменная объявлена в модуле
    # но эту переменную сейчас нельзя изменить
    # локально это ругая переменная
    global_var = 999
    print('"global" in local', global_var)


my_f()
print('global in global', global_var)
# локальная переменная недоступна недоступна вне функции
# print('local in global', local_var)
