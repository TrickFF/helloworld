# строка байт
#sb = b'Ad'

# по ascii таблице должно получиться 65
#print(sb[0])
# по ascii таблице должно получиться 100
#print(sb[1])

s = 'Helo World Мир'

sb = s.encode('utf-8')

print(sb)
print(type(sb))

st = sb.decode('utf-8')
print(st)
print(type(st))