from sys import stdin
from collections import defaultdict
input = stdin.readline

for _ in range(int(input())):
    n,x,y = list(map(int, input().split()))
    a = list(map(int, input().split()))

    dsu = [-1]*(n+1)

    def find(x):
        while dsu[x] >= 0:
            while dsu[dsu[x]] >= 0:
                dsu[x] = dsu[dsu[x]]
            x = dsu[x]
        
        return x

    def merge(x, y):
        x = find(x)
        y = find(y)

        if x == y: return

        if dsu[x] <= dsu[y]:
            # x becomes parent
            dsu[x] += dsu[y]
            dsu[y] = x
        else:
            # y becomes parent
            dsu[y] += dsu[x]
            dsu[x] = y

    for i in range(n):
        if i+x < n: merge(i, i+x)
        if i+y < n: merge(i, i+y)
    
    set_vals, set_idxs = defaultdict(list), defaultdict(list)
    for i in range(n):
        set_vals[find(i)].append(a[i])
        set_idxs[find(i)].append(i)
    
    for i in range(len(set_vals)):
        set_vals[i].sort()
        set_idxs[i].sort()

        for j in range(len(set_vals[i])):
            a[set_idxs[i][j]] = set_vals[i][j]

    if a == sorted(a):
        print("YES")
    else:
        print("NO")