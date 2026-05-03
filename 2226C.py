for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)

    l,r = 0, n
    while (l < r):
        cnt = (l+r+1)//2
        mex = cnt-1
        # print("checking", cnt)

        freq = {}
        for x in a:
            freq[x] = freq.get(x, 0) + 1
            
        for x in a:
            # print('checking mex:', mex, ", against x:", x, freq)
            while freq.get(mex, 0) > 0:
                freq[mex] -= 1
                mex -= 1
            if freq[x] > 0 and mex <= (x-1)//2:
                freq[x] -= 1
                mex -= 1

            if mex < 0: break
        
        if mex < 0: 
            l = cnt
        else:
            r = cnt-1
            # print('failed cnt=', cnt)
    
    print(l)