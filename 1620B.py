for i in range(int(input())):
    w,h = list(map(int, input().split()))
    x1 = list(map(int, input().split()))[1:]
    x2 = list(map(int, input().split()))[1:]
    y1 = list(map(int, input().split()))[1:]
    y2 = list(map(int, input().split()))[1:]

    ans = 0
    for i in [x1,x2]:
        ans = max(ans, (max(i)-min(i))*h)
    for i in [y1,y2]:
        ans = max((max(i)-min(i))*w, ans)
    
    print(ans)
