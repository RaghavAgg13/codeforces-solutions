for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if n == 1:
        print(0)
        continue

    xor = 0
    for i in a: xor ^= i

    if xor == 0:
        print(1)
    else:
        ways = 0
        for i in range(n):
            if xor^a[i] < a[i]: ways += 1

        print(ways)