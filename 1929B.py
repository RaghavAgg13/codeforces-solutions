from math import ceil
for i in range(int(input())):
    n,k = list(map(int, input().split()))

    c = ceil(k/2)
    if k == 4*n-2: c += 1
    print(c)