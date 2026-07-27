for _ in range(int(input())):
    n,k = list(map(int, input().split()))
    s = input()

    if 2*k > n:
        print(-1)
        continue

    cnt = 0
    for i in range(k):
        if s[i] == "L": cnt += 1
    
    for i in range(n-1, n-k-1, -1):
        if s[i] == "R": cnt += 1
    
    print(cnt)