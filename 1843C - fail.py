from math import log
for i in range(int(input())):
    n = int(input())

    lvl = int(log(n, 2))
    base = 2**(lvl+1)-1

    for i in (lvl+1):
        