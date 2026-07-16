for _ in range(int(input())):
    n,d = list(map(int, input().split()))
    a = list(map(int, input().split()))

    a = a+a+a
    pref = [0]*(3*n+1)
    for i in range(3*n):
        pref[i+1] = pref[i]+a[i]

    ans = 0

    for i in range(n, 2*n):
        l,r = i-d, i+d

        window_sum = pref[r+1]-pref[l]
        delta = a[i]*(2*d+1) - window_sum

        if delta > 0: ans += delta

    print(ans)
