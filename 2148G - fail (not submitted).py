from math import gcd
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    print(0, end = ' ')
    gcd_max = 0
    idx = 0
    for i in range(1, n):

        gcd_cur = a[0]
        for j in range(1, i):
            gcd_temp = gcd(gcd_cur, a[j])
            if gcd_cur > gcd_temp:
                gcd_cur = gcd_temp
                
                if gcd_max < gcd_cur:
                    idx = j+1
                    gcd_max = gcd_cur


        print(idx, end=' ')
    print()