from math import ceil
for i in range(int(input())):
    n,m,d = list(map(int, input().split()))


    stack = d//m + 1
    print(ceil(n/stack))