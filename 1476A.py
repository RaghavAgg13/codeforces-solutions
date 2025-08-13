from math import ceil
for i in range(int(input())):
    n,k= list(map(int, input().split()))

    print((((n+k-1)//k)*k+n-1)//n)