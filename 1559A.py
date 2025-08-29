for i in range(int(input())):
    n = int(input())
    a = list(set(map(int, input().split())))
    n = len(a)

    xor = a[0]
    for i in range(1, n): xor &= a[i]
    print(xor)