for i in range(int(input())):
    n,m = list(map(int, input().split()))
    a = input()
    b = input()

    c = a+b[::-1]
    n1 = 0
    for i in range(n+m-1):
        if c[i] != c[i+1]: n1 += 1

    if abs(n+m-n1) <= 2: print('YES')
    else: print('NO')