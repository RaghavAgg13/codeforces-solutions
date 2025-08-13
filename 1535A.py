for i in range(int(input())):
    a,b,c,d = list(map(int, input().split()))
    s = sorted([a,b,c,d])

    print('YES' if sorted([max(a,b), max(c,d)]) == s[2:] else 'NO')