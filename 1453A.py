for i in range(int(input())):
    n,m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    n1 = len(a)+len(b)
    c = set(a+b)
    n2 = len(c)
    print(n1-n2)