for i in range(int(input())):
    n = int(input())
    arr = []

    for i in range(n):
        a = list(map(int, input().split()))
        arr.append(a)

    ans = 0
    for i in range(n-1, -1, -1):
        c,p = arr[i]

        ans = max(ans, c + (1-p/100)*ans)
    
    print(ans)