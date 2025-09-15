for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    b = list(sorted(a))
    count = 0
    while a != b:
        for i in range(0,n-1, 2):
            if a[i] > a[i+1]: a[i], a[i+1] = a[i+1], a[i]
        count += 1
        if a == b: break
        for i in range(1, n, 2):
            if a[i] > a[i+1]: a[i], a[i+1] = a[i+1], a[i]
        count += 1

    print(count)