# слово -> СлОвО

word = 'слово'
result = []
for l in range(len(word)):
    if l % 2 != 0:
        letter = word[l].lower()
    else:
        letter = word[l].upper()
    result.append(letter)

print(result)
result = ''.join(result)
print(result)

# с тернарным оператором
word = 'Привет'
result = []
for l in range(len(word)):
    letter = word[l]
    letter = letter.lower() if l % 2 != 0 else letter.upper()
    result.append(letter)

print(result)
result = ''.join(result)
print(result)
