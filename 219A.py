from collections import Counter
k = int(input())
a = input()

b = Counter(a)

check = True
c = ''
for key,val in b.items():
    if val%k:
        check = False
        break
    else:
        c += key*(val//k)

print(c*k if check else -1)
