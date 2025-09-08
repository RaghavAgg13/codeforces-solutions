for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    d = [b[0]-a[0]]
    for i in range(1, n):
        d.append(b[i]-max(b[i-1], a[i]))

    print(*d)