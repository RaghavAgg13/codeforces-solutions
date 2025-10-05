for i in range(int(input())):
    n,m = list(map(int, input().split()))
    if m == n == 1: print(0)
    else: print(n+m+min(n,m)-2)