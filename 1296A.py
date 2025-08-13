for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))

    counto = 0
    for i in l:
        if i%2 == 1: counto += 1

    if (n> counto > 0) or sum(l)%2 == 1: print('YES')
    else: print('NO')