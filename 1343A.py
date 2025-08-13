from math import log2
for i in range(int(input())):
    n = int(input())

    if int(log2(n+1)) == log2(n+1):
        print('1')
    else:
        for k in range(2, int(log2(n+1))+1):
            x = n/((2**k) - 1)
            if int(x) == x:
                x = int(x)
                print(x)
                break