for i in range(int(input())):
    a = list(input())
    n = len(a)

    # for i in range(0, n, 2):
    #     if a[i] != 'a': a[i] = 'a'
    #     else: a[i] = 'b'

    # for i in range(1, n, 2):
    #     if a[i] != 'z': a[i] = 'z'
    #     else: a[i] = 'y'

    # print(*a, sep='')

    d = ''
    for i in range(0, n):
        if not i%2:
            if a[i] != 'a': d = 'a'
            else: d = 'b'
        else:
            if a[i] != 'z': d = 'z'
            else:d = 'y'

        print(d, end='')
    print()