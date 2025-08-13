for i in range(int(input())):
    a,b = list(map(int, input().split()))

    if a == b*2 or (2*b>a and (2*b-a)%2 == 0 and a!=0 and b!=0) or (a>b*2 and (a-b*2)%2 == 0 and a!=0 and b!=0) or (a%2==0 and b==0) or (a==0 and b%2==0):
        print('YES')
    else: print('NO')