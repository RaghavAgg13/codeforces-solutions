for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    good = [[0]*(n+1) for _ in range(n+1)]

    for i in range(n):
        mi, ma = a[i], a[i]
        dups = [0]*(n+1)

        for j in range(i, n):
            if dups[a[j]]: break
            dups[a[j]] = 1

            mi, ma = min(mi, a[j]), max(ma, a[j])
            if ma-mi == j-i: good[mi][ma] = 1
    
    for ans in range(n, -1, -1):
        if ans%2: continue
        found = False
        for i in range(1, n+1):
            if i+ans-1 > n: break

            if good[i][i+ans//2-1] and good[i+ans//2][i+ans-1]:
                found = ans//2
                break

        if found is not False: break

    print(found if found != False else 0) 