from math import log2
for _ in range(int(input())):
    n,k = list(map(int, input().split()))

    upper = n//k

    if k >= n:
        print(n)
        continue

    if upper:
        a = (upper+1).bit_length()-1
    else: a = 0

    ans = a*k
    rem = n - (2**a-1)*k


    if rem >= 2**a:
        ans += (rem//(2**a))


    print(ans)