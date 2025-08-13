t = int(input())

for i in range(t):
    n = int(input())
    s = sorted(list(map(int, input().split(' '))))

    while n > 1:
        i=1
        if abs(s[i] - s[i-1]) <= 1:
            s.remove(min(s[i], s[i-1]))
            n -= 1
            i += 1
        else:
            break
    if n == 1:
        print('YES')
    else:
        print('NO')
    