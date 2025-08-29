t = int(input())
for i in range(t):
    b = True
    n = int(input())
    s = sorted(list(map(int, input().split())))

    for i in range(n):
        if sum(s[:i+1])%2 == sum(s[1+i:])%2:
            print('YES')
            b  = False
            break

    if b: print('NO') 