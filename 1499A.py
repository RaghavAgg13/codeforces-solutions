for i in range(int(input())):
    n,k1,k2 = list(map(int, input().split()))
    w,b = list(map(int, input().split()))

    if (k1+k2)//2 >= w and (2*n-k1-k2)//2 >= b:
        print('YES')
    else:
        print('NO')