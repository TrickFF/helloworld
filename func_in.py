def my_f(my_var):
    my_var = 999
    print('Внутри функции:', my_var)

a = 1
my_f(a)
print('После выполнения функции:', a)

print('-'*60)

def some_f():
    a = 999
    print('Внутри функции:', a)

a = 1
some_f()
print('После выполнения функции:', a)