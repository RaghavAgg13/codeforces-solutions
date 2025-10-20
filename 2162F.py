for i in range(int(input())):
    n,m = list(map(int, input().split()))

    arr = [i for i in range(n)]

    for i in range(m):
        l,r = list(map(int, input().split()))

        for j in range(l-1, r):
            if j in arr: arr.remove(j)
        
    if arr == []:
        print(*[i for i in range(n)])
    else:
        print(*[i for i in range(arr[0])], n-1, *[i for i in range(arr[0]+1,n-1)], end=' ')
        print()