s = ['a', 'e', 'i', 'o', 'u', 'y']
a = input()
a.lower()

b = ''
for i in a:
    if i not in s:
        b += i

for i in b:
    print('.', i, end='', sep='')