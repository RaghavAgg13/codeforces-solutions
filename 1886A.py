for i in range(int(input())):
    n = int(input())
    if n < 6:
        print('NO')
    elif n%3 and n-3 != 2 and n-3 != 1:
        print('YES')
        print(1,2,n-3)
    elif (n-5)%3 and n-5 != 4 and n-5 != 1:
        print('YES')
        print(1,4,n-5)
    else: print('NO')