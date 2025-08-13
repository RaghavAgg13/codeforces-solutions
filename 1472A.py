for i in range(int(input())):
    w,h, n = list(map(int, input().split()))

    count = 1

    # if w == 1 and h == 8 and n == 8: print('BOINK')
    while w%2 == 0:
        w /= 2
        count *= 2

    while h%2 == 0:
        h /= 2
        count *= 2

    print('YES' if count >= n else 'NO')