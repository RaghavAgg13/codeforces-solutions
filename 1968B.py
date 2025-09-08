for i in range(int(input())):
    n,m = list(map(int, input().split()))
    a = input()
    b = input()

    k = 0
    for i in a:
        if i in b:
            k += 1
            b = b[b.index(i)+1:]
        else: break

    print(k)