def sep():
    print('-' * 100)

def hello_max():
    print('Hello, Max!')

hello_max()
sep()

def hello(who):
    print(f'Hello, {who}!')

hello('Sergey')
hello('Max')
sep()

def greeting(who, say):
    print(f'{say}, {who}!')

greeting('Hi','Sergey')
greeting('Sergey', 'Hi')
greeting(say='Hi',who='Sergey')
sep()

def greeting(who, say='Welcome'):
    print(f'{say}, {who}!')

greeting('Sergey', 'Hi')
greeting('Sergey')