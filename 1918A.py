for i in range(int(input())):
    n,m = list(map(int, input().split()))

    if m%2 == 0:
        print(n*m//2)
    else:
        print(n*(m//2-1)+n)