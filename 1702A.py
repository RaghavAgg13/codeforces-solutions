from math import log10
from math import ceil
for i in range(int(input())):
    n = int(input())
    log = max(ceil(log10(n))-1, 0)
    if log10(n) == int(log10(n)):
        print(0)
    else:
        print(n-10**log)