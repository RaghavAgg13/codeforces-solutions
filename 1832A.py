for i in range(int(input())):
    a = input()

    b = 0
    for i in set(a):
        if a.count(i) > 1: b += 1

    if b > 1: print('YES')
    else: print('NO')