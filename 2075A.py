for i in range(int(input())):
    n,k = list(map(int, input().split()))

    count = 1 + (n-k)//(k-1)
    n = (n-k)%(k-1)
    count += 1 if n else 0

    print(count)