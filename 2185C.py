for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    b = sorted(set(a))
    m = b[0]

    cnt = 1
    m = 0
    for i in range(1, len(b)): 
        if b[i]-b[i-1] > 1:
            m = max(cnt, m)
            cnt = 1
        else: cnt += 1
    
    m = max(cnt, m)
    print(m)