from math import isqrt
for i in range(int(input())):
    n = int(input())
    
    pow2 = isqrt(n)
    
    pow3_guess = int(n**(1/3))
    pow3 = pow3_guess
    if (pow3_guess + 1)**3 <= n:
        pow3 += 1
    elif pow3_guess**3 > n:
        pow3 -= 1

    sixth_guess = int(n**(1/6))
    pow6 = sixth_guess
    if (sixth_guess + 1)**6 <= n:
        pow6 += 1
    elif sixth_guess**6 > n:
        pow6 -= 1

    print(pow2 + pow3 - pow6)