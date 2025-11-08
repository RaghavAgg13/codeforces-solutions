from math import log, ceil

for _ in range(int(input())):
    a, b = map(int, input().split())

    if b > a:
        print(1)
    elif b == a:
        print(2)
    else:
        if b != 1:
            ini = ceil(log(a, b) + 1e-12)
        else:
            ini = ceil(1 + log(a, b + 1) + 1e-12)

        # print('initial ini is', ini)

        for i in range(1, min(ini, 21)):
            ini = min(ini, i + ceil(log(a, b + i) + 1e-12))

            # print('transitional ini is', ini, 'at i =', i)

        print(ini)
