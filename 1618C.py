from math import gcd
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    gcd1,gcd2 = a[0], a[1]
    for i in range(2, n):
        if not i%2: gcd1 = gcd(gcd1, a[i])
        else: gcd2 = gcd(gcd2, a[i])
    
    # print('gcd is', gcd1, gcd2)
    if gcd1 != gcd2 and max(gcd1, gcd2) != 1: 
        check = False if gcd2 == 1 else True
        if check:
            for i in range(0,n,2):
                if not a[i]%gcd2:
                    check = False
                    break

        if check: 
            print(gcd2)
            continue

        check = False if gcd1 == 1 else True
        if check:
            for i in range(1, n, 2):
                if not a[i]%gcd1:
                    check = False
                    break
        
        if check: 
            print(gcd1)
            continue
    
    print(0)