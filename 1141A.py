n,m = list(map(int, input().split()))
if (m%n == 0 and ((m/n)%2 == 0 or (m/n)%3 == 0)) or n==m:
    a = m//n
    count = 0
    while a%2 == 0:
        a //= 2
        count += 1
    while a%3 == 0:
        a //= 3
        count += 1

    if a!=1:
        print(-1)
    else:
        print(count)
else:
    print(-1)