a = input()

cnt = a.count('b')
b = {'B':1, 'u':2, 'l':1, 'a':2, 's':1, 'r':1}

items = []
for key,val in b.items():
    cnt = min(cnt, a.count(key)//val)

print(cnt)