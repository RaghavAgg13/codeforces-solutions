for _ in range(int(input())):
    n = int(input())
    a = []

    colors = [0]*(n**2+1)
    
    for _ in range(n):
        arr = list(map(int, input().split()))
        a.append(arr)

        for color in arr:
            colors[color] += 1
    
    for count in colors:
        if count > n*(n-1):
            print("NO")
            break
    else:
        print("YES")