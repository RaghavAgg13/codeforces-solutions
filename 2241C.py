for _ in range(int(input())):
    n = int(input())
    a = input()

    f = True
    while f:
        f = False
        while '00' in a:
            a = a.replace("00", "0")
            f = True
        while '11' in a:
            a = a.replace('11', '1')
            f = True

    if len(a) > 2:
        print(1)
    else:
        print(len(a))        