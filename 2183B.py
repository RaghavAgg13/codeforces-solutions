for i in range(int(input())):
    n,k = list(map(int, input().split()))
    a = set(map(int, input().split()))
    
    mex = 0
    for i in range(k-1):
        if i in a:
            mex += 1
        else: break

    print(mex)