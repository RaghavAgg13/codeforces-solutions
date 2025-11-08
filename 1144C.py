from collections import Counter
n = int(input())
a = list(map(int, input().split()))

x,y = [], []
n1, n2 = 0,0
b = Counter(a)
for i,k in b.items():
    x.append(i)
    n1 += 1
    if k == 2: 
        y.append(i)
        n2 += 1
    elif k > 2: 
        print('NO')
        break
else:
    print('YES')
    print(n1)
    print(*sorted(x))
    print(n2)
    print(*sorted(y, reverse=True))