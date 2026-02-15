for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    ans = []
    dist = 0
    x,y = a[0], a[n]
    for i in range(n):
        ans.append([a[i], a[n+i]])
        dist += abs(x-a[i]) + abs(y-a[n+i])
        x,y = a[i], a[n+i]  
    
    print(dist)
    for i in ans:
        print(*i)

    
