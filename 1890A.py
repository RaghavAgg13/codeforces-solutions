for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    unq = list(set(l))

    b = False
    if len(unq) == 2:
        if n%2 == 0:
            if l.count(unq[0]) == l.count(unq[1]):
                b = True
        else:
            if abs(l.count(unq[0]) - l.count(unq[1])) == 1:
                b = True
    elif len(unq) == 1:
        b = True

    print('YES' if b else 'NO')