for i in range(int(input())):
    n,a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    prod = 1
    for i in b: prod *= i
    
    if 2023%prod == 0: 
        print('YES')
        print(2023//prod, end=' ')
        for i in range(a-1): print(1, end=' ')
        print()

    else: print('NO')