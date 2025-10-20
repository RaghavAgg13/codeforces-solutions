from math import ceil, log2

for _ in range(int(input())):
    a, b = map(int, input().split())

    n1 = len(bin(a))
    n2 = len(bin(b))

    if a == b:
        print(0)
    elif n1 >= n2:
        ans= a^b
        n = int(log2(a))
        bin_a = bin(ans)[2:]
        nos = [int(bin_a[-n:], 2)]

        for i in range(1, ceil(len(bin_a)/n)):
            nos.append(int(bin_a[-i*n-n:-i*n], 2)<<(i*n))

        print(len(nos))
        print(*nos)
    else:
        print(-1)