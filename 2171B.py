for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if a[0] != -1 and a[-1] == -1:
        a[-1] = a[0]
    elif a[-1] != -1 and a[0] == -1:
        a[0] = a[-1]
    elif a[-1] == -1 and a[0] == -1:
        a[0] = a[-1] = 0
    for i in range(1,n-1):
        if a[i] == -1: a[i] = 0

    print(abs(a[0]-a[-1]))
    print(*a)