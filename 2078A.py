from math import log
for i in range(int(input())):
    n,x = list(map(int, input().split()))
    a = list(map(int, input().split()))

    check = False
    s = sum(a)

    if not s%x:
        s //= x
        if log(s/n) == int(log(s/n)):
            check = True

    print('YES' if check else 'NO')