for i in range(int(input())):
    x,y = list(map(int, input().split()))

    x,y = x-min(x,y)+1, y-min(x,y)+1
    if y == x+1 or (not x%9 and y == 1): print('Yes')
    else: print('No')