for i in range(int(input())):
    a,b,n = list(map(int, input().split()))

    count = 0
    while max(a,b) <= n:
        count += 1
        if a == max(a,b):
            b += a
        else: a += b

    print(count)