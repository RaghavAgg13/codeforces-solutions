for i in range(int(input())):
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    arr = [[b[i], i+1] for i in range(n)]
    arr.sort(reverse=True)

    ans = []
    for course in arr:
        if course[0] <= k:
            ans.extend(([course[1]]*(k+1-course[0])))
        
        if (len(ans) > 1000): break
    
    if (len(ans) > 1000):
        print(-1)
    else:
        print(len(ans))
        print(*ans)
    