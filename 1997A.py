for i in range(int(input())):
    a = input()
    n = len(a)

    check = True
    for i in range(1, n):
        if a[i] == a[i-1]:
            check = False
            if 'a' != a[i]:
                print(a[:i], 'a', a[i:], sep='')
            else:
                print(a[:i], 'b', a[i:], sep='')
            break
    
    if check:
        if 'a' != a[0]:
            print('a', a, sep='')
        else:
            print('b', a, sep='')