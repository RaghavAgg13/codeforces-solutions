from math import isqrt
for i in range(int(input())):
    n = int(input())
    factors = []

    for a in range(2, isqrt(n) + 1):
        if n%a == 0:
            factors.append(a)
            n //= a
            break

    if not factors:
        print('NO')
        continue

    for b in range(factors[-1]+1, isqrt(n)+1):
        if n%b == 0 and b != factors[-1]:
            factors.append(b)
            n//=b
            break

    c = n
    if len(factors) == 2 and c > factors[1] and c != factors[0]:
        factors.append(c)
        print("YES")
        print(*factors)
    else:
        print("NO")
