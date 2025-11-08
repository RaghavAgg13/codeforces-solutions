n = int(input())
a = sorted(list(map(int, input().split())))


print(n//2 if n%2 else n//2-1)
for i in range(1, n//2+1):
    print(a[n//2+i-1], a[i-1], end=' ')
if n%2: print(a[n-1])