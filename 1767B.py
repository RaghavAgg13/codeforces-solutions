from math import ceil
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    b = a[0]
    a = sorted(a[1:])
    a.insert(0, b)

    for i in range(n):
        if a[0] < a[i]:
            a[0], a[i] = ceil((a[0]+a[i])/2), (a[0]+a[i])//2
    
    print(a[0])