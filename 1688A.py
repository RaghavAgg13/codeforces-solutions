from math import log2
for i in range(int(input())):
    n = int(input())

    ans = 0
    for i in range(int(log2(n))+2):
        if n&(2**i) > 0:
            ans += 2**i
            break
    for i in range(-1, ans+1):
        if n^(ans+int(2**i)) > 0:
            ans += int(2**i)
            break
    print(ans + bool(n==1))