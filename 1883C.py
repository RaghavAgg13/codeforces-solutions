for i in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    soln = k
    if k == 4:
        #rem = 4k, 2k-1, 2k, 4k-1
        rem = [0,0,0,0]

        for i in a: rem[i%4] += 1

        if rem[0] >= 1 or rem[2] >= 2:
            soln = 0
        elif rem[3] >= 1:
            soln = 1
        elif rem[2] !=0 and rem[1] != 0:
            soln = 1
        elif rem[2] == 0 and rem[1] >= 2:
            soln = 2

    else:
        for j in a:
            if j%k==0:
                soln = 0
                break
            soln = min(soln, k -(j%k))

    print(soln)