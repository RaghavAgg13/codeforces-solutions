for i in range(int(input())):
    a,b = list(map(int, input().split()))

    a,b = min(a,b), max(a,b)

    print('YES' if not b%a else 'NO')