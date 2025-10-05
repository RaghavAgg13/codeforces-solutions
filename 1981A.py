from math import log2
for i in range(int(input())):
    a,b = list(map(int, input().split()))
    print(int(log2(b)))