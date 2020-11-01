def some_f():
    return 10


result = some_f()
print(result)

# В переменную a записывается сама функция, а не ее результат
# т.е. какой-то адрес в памяти
a = some_f
print(a)
print(type(a))
# т.о. функция в python также является объектом
print(a())
