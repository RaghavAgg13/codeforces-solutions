for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    s = sum([i for i in a if i != 1])

    if a[-1] == 1: s += 1

    print(s)