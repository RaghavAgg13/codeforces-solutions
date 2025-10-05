from math import log2
for i in range(int(input())):
    n = int(input())

    pos = 2**(int(log2(n)))
    print(pos)