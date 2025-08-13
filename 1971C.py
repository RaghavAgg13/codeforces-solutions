for i in range(int(input())):
    a,b,c,d = list(map(int, input().split()))
    a,b = min(a,b), max(a,b)
    if (a < c < b and not(a < d < b)) or (a < d < b and not(a < c < b)):
        print('YES')
    else: print('NO')