for i in range(int(input())):
    n,m = list(map(int, input().split()))

    if n%2 == m%2:
        print('Tonya')
    else:
        print('Burenka')