from math import ceil
for i in range(int(input())):
    p,a,b,c = list(map(int, input().split()))

    n1 = (a-p%a)%a
    n2 = (b-p%b)%b
    n3 = (c-p%c)%c
    print(min(n1,n2,n3))