def f():
    print('hello from other f')


def to(f_param):
    # параметром будет функция
    # поэтому в теле функции to мы ее вызовем
    f_param()


def to2(f):
    # параметром будет функция
    # поэтому в теле функции to мы ее вызовем
    f()


# проверим
to(f)
to2(f)
