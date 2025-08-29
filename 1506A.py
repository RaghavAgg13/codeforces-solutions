for i in range(int(input())):
    n,m,x = list(map(int, input().split()))

    b = x//n + bool(x%n)
    a = x%n if x%n != 0 else n
    y = (a-1)*m+b
    print(y)