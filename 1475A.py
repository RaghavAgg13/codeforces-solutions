t = int(input())


for i in range(t):
    b = False
    n = int(input())
    
    while n % 2 == 0:
        n /= 2
    if n <= 2:
        print('NO')
    else:
        print('YES')