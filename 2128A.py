for i in range(int(input())):
    n,c = list(map(int, input().split()))
    a = list(map(int, input().split()))

    a.sort()
    count = 0
    for i in range(n-1, -1, -1):
        if a[i]*(2**(count)) <= c:
            count += 1

    print(n-count)