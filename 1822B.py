for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))


    if n == 2:
        print(a[0]*a[1])
    elif n == 3:
        a.sort()
        print(max(a[0]*a[1], a[1]*a[2]))
    else:
        b = max(a)
        a.remove(b)

        c = min(a)
        a.remove(c)
        print(max(b*max(a), c*min(a)))
