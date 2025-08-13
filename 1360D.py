import math
for i in range(int(input())):
    n,k = list(map(int, input().split()))

    def is_prime(num):
        if num <= 1:
            return False
        if num %2 == 0:
            return num == 2
        
        
        for i in range(3, math.isqrt(num) + 1, 2):
            if num % i == 0:
                return False
        return True

    if k >= n:
        print(1)
    elif k == 1:
        print(n)
    elif is_prime(n):
        print(n)
    elif n%k == 0:
        print(n//k)
    else:
        ans = n
        limit = min(k, math.isqrt(n))
        for i in range(limit, 1, -1):
            if n % i == 0:
                if i <= k:
                    ans = min(ans, n // i)
                if n // i <= k:
                    ans = min(ans, i)

        print(ans)