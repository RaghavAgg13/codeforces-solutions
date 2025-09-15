for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    start = a.index(1)
    end = a[::-1].index(1)
    count = a[start:n-end].count(0)
    print(count)