for i in range(int(input())):
    n,t = list(map(int, input().split()))

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    final = -1
    idx = -1
    for i in range(n):
        if a[i]+i <= t:
            if b[i] > final:
                final = b[i]
                idx = i+1

    print(idx)