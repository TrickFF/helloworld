# функция с возвращаемым результатом

# return - возвращаемый результат
def get_sep(sep, sep_len):
    return sep * sep_len


print(get_sep('-', 40))
print(get_sep('+', 70))
print(get_sep('/', 55))

sep1 = get_sep('-', 50)
#text = 'Hello {} Func {}'.format(sep, sep)
text = f'Hello {sep1} Function {sep1}'
print(text)