from math import log2
for i in range(int(input())):
    n = int(input())

    if n == 1: print(1)
    else: print(2+int(log2((n+1)//3)))