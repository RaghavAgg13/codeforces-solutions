for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    start = 1
    i = 0
    while i < n:
        if i < n-1 and a[i] == 0 and a[i+1] == 0:
            start = -1
            break
        elif i < n-1 and a[i] == 1 and a[i+1] == 1:
            start += 5
        elif a[i] == 1 : start += 1
        i += 1
    print(start)