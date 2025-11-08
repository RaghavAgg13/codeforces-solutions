for i in range(int(input())):
    n = int(input())

    print('9'*(n-n//4-bool(n%4)), '8'*(n//4+bool(n%4)), sep='')