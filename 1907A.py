for i in range(int(input())):
    a = input()

    p1 = a[0]
    p2 = int(a[1])

    for i in range(1, 9):
        if i != p2: print(p1, i, sep='')
    for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        if i != p1: print(i, p2, sep='')