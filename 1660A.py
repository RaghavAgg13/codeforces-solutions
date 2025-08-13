for i in range(int(input())):
    a,b = list(map(int, input().split()))

    if (a==0 and b==0) or (a==0 and b!=0):
        m = 1
    elif b == 0:
        m = a+1
    else:
        m = a+b*2+1

    print(m)