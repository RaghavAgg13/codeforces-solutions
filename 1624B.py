for i in range(int(input())):
    a,b,c = list(map(int, input().split()))

    if ((a+c)//2)//b >= 1 and ((a+c)//2)%b == 0 and (a+c)%2 == 0:
        print('YES')
    elif (2*b - c)//a >= 1 and (2*b - c)%a == 0:
        print('YES')
    elif (2*b - a)//c >= 1 and (2*b - a)%c == 0:
        print('YES')
    else:
        print('NO')