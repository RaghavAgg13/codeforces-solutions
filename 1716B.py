for i in range(int(input())):
    n = int(input())
    a = [i+1 for i in range(n)]

    print(n)
    print(*a)
    for i in range(n-1):
        a[i],a[-1] = a[-1], a[i]
        print(*a)
        # a[i],a[-1] = a[-1], a[i]