from math import ceil
for i in range(int(input())):
    n,k = list(map(int, input().split()))

    if n >= k and (n % 2 == k % 2):
        print("YES")
        res = [1] * (k - 1)
        res.append(n - (k - 1))
        print(*res)
    elif n >= 2 * k and n % 2 == 0:
        print("YES")
        res = [2] * (k - 1)
        res.append(n - 2 * (k - 1))
        print(*res)
    else:
        print("NO")