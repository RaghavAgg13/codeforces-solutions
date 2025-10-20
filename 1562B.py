for i in range(int(input())):
    n = int(input())
    a = input()

    check = True
    for i in ['1', '4', '6', '8', '9']:
        if i in a:
            print(1)
            print(i)
            check = False
            break

    if check:
        for i in ['2', '5']:
            if i in a[1:]:
                print(2)
                print(a[0], i, sep='')
                check = False
                break
    
    if check:
        if a.count('3') > 1:
            print(2)
            print(33)
            check = False
        elif a.count('7') > 1:
            print(2)
            check = False
            print(77)
        elif '2' in a and '7' in a:
            print(2)
            check = False
            print(27)
        elif '3' in a and '5' in a[a.index('3'):]:
            print(2)
            check = False
            print(35)
        elif '5' in a and '7' in a:
            print(2)
            print(57)
            check = False
    
    if check:
        print(n)
        print(a)