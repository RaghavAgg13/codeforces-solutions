for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    bit = a[0]
    for i in range(1, n):
        bit ^= a[i]
        if not bit:
            print(a[i])
            break