for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    suma = (a[0]+a[-1])//(n-1)

    # print('degbug', suma)

    arr = []
    cum_sum = 0
    for i in range(n-1):
        val = (suma-(a[i]-a[i+1]))//2
        arr.append(val-cum_sum)
        
        cum_sum += arr[-1]

    arr.append(suma-sum(arr))

    print(*arr)
