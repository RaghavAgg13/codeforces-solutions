for i in range(int(input())):
    n,k = list(map(int, input().split()))

    min = k**2
    if n < min or n%2 != k%2:
        print('NO')
    else:
        print('YES')