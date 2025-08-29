from math import ceil
from math import log2
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    count = 0
    for i in range(1, n):
        n1, n2 = max(a[i], a[i-1]), min(a[i], a[i-1])
        if n1 > 2*n2:
            delta = n1/n2
            count += ceil(log2(delta)) - 1
        
    print(count)