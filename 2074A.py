for i in range(int(input())):
    l,r,d,u = list(map(int, input().split()))

    print('YES' if l==r==d==u else 'NO')