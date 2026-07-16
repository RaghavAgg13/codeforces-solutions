from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(1, n):
        if a[i-1] > a[i]:
            a[i-1],a[i] = a[i], a[i-1]+a[i]
            for j in range(i+1, n):
                if a[j-1] > a[j]:
                    a[j-1],a[j] = a[j], a[j-1]+a[j]
            break

    print(a[-1])
