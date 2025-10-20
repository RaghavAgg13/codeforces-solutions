from math import log2, pow
for i in range(int(input())):
    n = int(input())

    if n%2: print('NO')
    else:
        if (not n%4 and int(pow(n//4, 0.5)) == pow(n//4, 0.5)) or (not n%2 and int(pow(n//2, 0.5)) == pow(n//2, 0.5)):
            print('YES')
        else:
            print('NO')