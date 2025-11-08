from math import gcd
for i in range(int(input())):
    s = input()
    t = input()

    if set(s) == set(t):
        n1,n2 = len(s), len(t)       

        if n1*t == n2*s:
            print(t*(n1//gcd(n1,n2)))
        else:
            print(-1)

    else:
        print(-1)