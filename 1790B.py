for i in range(int(input())):
    n,s,r = list(map(int, input().split()))

    m = s-r
    n -= 1
    a = [r//n]*(n)
    for i in range(r%n):
        a[i] += 1
    print(*a, end=' ')
    print(m)