for i in range(int(input())):
    n, k = list(map(int, input().split()))
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())), reverse=True)

    x = 0
    for i in range(k):
        x += max(a[i], b[i])
    x += sum(a[k:])
    print(x)