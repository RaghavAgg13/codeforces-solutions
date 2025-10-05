for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    sum = 0
    for i in range(n):
        if not i%2:
            sum += a[i]
        else: sum -= a[i]

    print(sum)