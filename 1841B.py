for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    b = [0]*n
    if n == 0:
        print()
        continue
    b[0] = 1

    c = [a[0]]
    cnt = 1
    drops = 0
    for j in range(1, n):
        x = a[j]
        if cnt == 1:
            new_drops = (1 if c[-1] > x else 0) + (1 if x > c[0] else 0)
        else:
            prev_wrap = 1 if c[-1] > c[0] else 0
            new_drops = drops - prev_wrap + (1 if c[-1] > x else 0) + (1 if x > c[0] else 0)

        if new_drops <= 1:
            c.append(x)
            cnt += 1
            drops = new_drops
            b[j] = 1
        else:
            b[j] = 0

    print(*b, sep='')