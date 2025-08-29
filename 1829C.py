for i in range(int(input())):
    n = int(input())
    s_01 = 400000
    s_10 = 400000
    s_11 = 400000

    for j in range(n):
        a,b = list(map(int, input().split()))
        if b == 1:
            s_01 = min(a,s_01)
        elif b == 10:
            s_10 = min(a,s_10)
        elif b == 11:
            s_11 = min(a,s_11)
        else: continue

    d = min(s_01+s_10, s_11)
    if (s_10 == 400000 or s_01 == 400000) and s_11 == 400000: print(-1)
    else: print(d)