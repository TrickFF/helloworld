m = 'm видно везде'

def a():
    ma = 'ma видно в b(),  a() и c()'
    def b():
        print('b - ', m)
        print('b - ', ma)
        mb = 'mb видно в b() и c(), но не видно в a()'
        def c():
            print('c - ', m)
            print('c - ', ma)
            print('c - ', mb)
            mc = 'mc видн отолько в c()'
            print('c - ', mc)
        c()
    b()
a()