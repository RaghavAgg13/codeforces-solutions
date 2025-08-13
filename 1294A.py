for i in range(int(input())):
    a,b,c,n = list(map(int, input().split()))
    a,b,c = sorted([a,b,c])

    print('YES' if (a+b+c+n)%3 == 0 and (2*c-a-b <= n) else 'NO')