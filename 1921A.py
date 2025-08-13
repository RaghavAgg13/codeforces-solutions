for i in range(int(input())):
    x,y = list(map(int, input().split()))
    x2,y2 = list(map(int, input().split()))
    input()
    input()
    
    if x != x2:
        area = abs(x-x2)**2
    else: area = abs(y-y2)**2
    print(area)