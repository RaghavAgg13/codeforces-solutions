for i in range(int(input())):
    n,m = list(map(int, input().split()))

    a = input()
    b = input()

    c = a + b[::-1]
    d = b + a[::-1]
    n1,n2 = 0,0
    for i in range(1, n+m):
        if c[i] == c[i-1]: n1 += 1
        if d[i] == d[i-1]: n2 += 1

    if (n1 <= 1 or n2 <= 1):
        print("YES")
    else:
        print("NO")