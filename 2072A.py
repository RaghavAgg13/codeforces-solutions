for i in range(int(input())):
    n,k,p = list(map(int, input().split()))
    k = max(k, -k)
    if k <= n*p:
        print(k//p + 1 if k%p!=0 else k//p)
    else:
        print(-1)