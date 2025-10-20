from math import isqrt
for i in range(int(input())):
    m,s = list(map(int, input().split()))
    b = list(map(int, input().split()))

    arrSum = sum(b)+s
    n = (-1+isqrt(1+8*arrSum))//2

    if isqrt(1+arrSum*8) != (1+8*arrSum)**0.5:
        print('NO')
        continue

    count,left = 0,s
    for i in range(1, n+1):
        if i not in b:
            if left >= i: 
                count += 1
                left -= i
            else:
                count = 0
                break

    print('YES' if count else 'NO')