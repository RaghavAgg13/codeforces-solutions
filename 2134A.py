for i in range(int(input())):
    n,a,b = list(map(int, input().split()))

    print('YES' if n%2==a%2==b%2 or (n%2==b%2 and a <= b) else 'NO')