for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    w1,w2 = [], []
    x,y = 0,0

    for i in range(n):
        if a[i] == 1:
            x += 1
            y += 1
        elif a[i] == 2:
            x -= 1
            y += 1
        else:
            x -= 1
            y -= 1
        
        w1.append(x)
        w2.append(y)

    mn = 10**9
    for i in range(n-1):
        if w2[i] >= mn:
            print("YES")
            break
        
        if w1[i] >= 0:
            mn = min(mn, w2[i])
    else:
        print("NO")
