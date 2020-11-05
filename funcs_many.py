m = 'm видно везде'

def a():
    print('a - ', m)
    ma = 'ma видно в b(),  a() и c()'
    print('a - ', ma)
    print()
    def b():
        print('b - ', m)
        print('b - ', ma)
        mb = 'mb видно в b() и c(), но не видно в a()'
        print('b - ', mb)
        print()
        def c():
            print('c - ', m)
            print('c - ', ma)
            print('c - ', mb)
            mc = 'mc видно отолько в c()'
            print('c - ', mc)
        c()
    b()
a()