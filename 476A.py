n, m = list(map(int, input().split()))
min = n//2 + n%2

if n >= m:
    if min%m != 0:
        print((1+(min//m))*m)
    else: print(min)
else: print('-1')