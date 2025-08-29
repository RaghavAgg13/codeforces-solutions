for i in range(int(input())):
    n,d = list(map(int, input().split()))
    a = input()

    if d == 0:
        print(int(a)*10)
    elif d == 9:
        print(9*(10**n) + int(a))
    else:
        check = False
        for i in range(n):
            if int(a[i]) < d:
                no = int(a[:i]+str(d)+a[i:])
                print(no)
                check = True
                break
        if not check: print(int(a+str(d)))