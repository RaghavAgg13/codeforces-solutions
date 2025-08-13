for i in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    s_min = min(s)
    for i in range(n):
        s[i] -= s_min
    print(sum(s))
