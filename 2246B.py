for _ in range(int(input())):
    n = int(input())

    if n == 2:
        print(-1)
        continue

    if n == 1:
        print(1)
        continue

    print(1, 2, end=' ')
    s = 3
    for i in range(2, n):
        print(s, end=' ')
        s *= 2
    print()