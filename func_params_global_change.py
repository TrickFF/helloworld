global_var = 1

def my_f():
    # изменение глобальной переменной локально
    global global_var
    # глобальная переменная объявлена в модуле
    print('global in local', global_var)
    global_var = 999
    print('global in local', global_var)


my_f()
print('global in global', global_var)
