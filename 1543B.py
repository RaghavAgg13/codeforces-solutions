for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    s = sum(a)
    rem = s%n

    ans = rem*(n-rem)
    print(ans)