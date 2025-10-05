for i in range(int(input())):
    n,k = list(map(int, input().split()))

    count = 0
    if k == 1: count,n = n, 0

    while n >= k:
        count += n%k
        n //= k

    print(count+n)