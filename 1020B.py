from sys import stdin
input = stdin.readline
n = int(input())
a = list(map(int, input().split()))

b = [0]*n
for i in range(n):
    c = i+1
    seen = []
    while c not in seen: 
        seen.append(c)
        c = a[c-1]
    b[i] = c

print(*b)