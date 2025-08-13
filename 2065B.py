for i in range(int(input())):
    a = input()
    n = len(a)

    b = False
    for i in range(n-2, -1, -1):
        if a[i] == a[i+1]:
            print(1)
            b = True
            break

    if not b: print(n)