for i in range(int(input())):
    p,q = list(map(int, input().split()))

    k = 2*p + 4*q + 1
    a = int(k**0.5)

    if a%2 == 0: a -= 1
    
    while k%a != 0:
        a -= 2
    
    if a > 1 and k//a-a <= 2*p:
        print(a//2, (k//a)//2)
    else:
        print(-1)