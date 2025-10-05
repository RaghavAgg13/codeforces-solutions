from math import sqrt
for i in range(int(input())):
    l,r = list(map(int, input().split()))

    diff = r-l

    n = int((-1+sqrt(1+8*diff))/2)
    print(n+1)