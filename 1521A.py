for i in range(int(input())):
    a,b = list(map(int, input().split()))
    soln = []
 
    check = False
    z_ = a*b
    i = 1
    while not check and i <= 4:
        z = z_*i
        j = 1
        while not check and j <= 4:
            x = a*j
            if x%z_ != 0 and (z-x)%z_ != 0:
                if z>x and z != x and x*2 != z and (z-x)%a == 0:
                    soln = [str(x), str(z-x), str(z)]
                    check = True
                    break
            j += 1
        i += 1
 
    if check:
        print('YES')
        print(' '.join(soln))
    else:
        print('NO')