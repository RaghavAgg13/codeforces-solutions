for i in range(int(input())):
    a = list(input())
    n = len(a)

    check = True
    for i in [0,n]:
        a.insert(i, 'a')
        if a != a[::-1]:
            print('YES')
            print(*a, sep='')
            check = False
            break
        else:
            a.pop(i)
    
    if check: print('NO')