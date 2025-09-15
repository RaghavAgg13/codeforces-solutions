for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    b = []

    for i in a:
        if i%2: print(i, end=' ')
        else: b.append(i)

    print(*b)