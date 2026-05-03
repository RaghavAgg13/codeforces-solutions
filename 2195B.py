for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    odds = (n+1)//2
    
    for i in range(1, n+1, 2):
        arr = []
        j = i
        while j <= n:
            arr.append(a[j-1])
            j *= 2
        
        arr.sort()
        
        p = i
        idx = 0
        while p <= n:
            a[p-1] = arr[idx]
            idx += 1
            p *= 2
        
    if a == sorted(a):
        print("YES")
    else:
        print("NO")