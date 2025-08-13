s = str.lower(input())
a = ''
for i in s:
    if i not in ['a', 'e', 'i', 'i', 'o', 'u', 'y']:
        a += '.'+ i
print(a)