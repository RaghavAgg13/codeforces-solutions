for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    check = 0
    for i in range(n):
        if b[i] < a[i]: check = 1
    count = 1 if check else 0

    while check:
        check = 0
        a.insert(0, 1)

        for i in range(n):
            if b[i] < a[i]: check = 1
        if check: count += 1

    print(count)