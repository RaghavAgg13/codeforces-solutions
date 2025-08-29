for i in range(int(input())):
    a,b = list(map(int, input().split()))

    d = max(a,b)-min(a,b)
    if d%2 == 1:
        print('Alice')
    else:
        print('Bob')