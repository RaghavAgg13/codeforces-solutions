for i in range(int(input())):
    n,m,i,j = list(map(int, input().split()))

    max = 0
    corners = [[1,m], [n,1], [n,m], [1,1]]
    for x1,y1 in corners:
        for x2,y2 in corners:
            dist = abs(i-x1)+abs(j-y1)+abs(x1-x2)+abs(y1-y2)+abs(x2-i)+abs(y2-j)
            if dist > max: 
                max = dist
                coords = [x1, y1, x2, y2]

    if [n,m,i,j] == [1,1,1,1]:
        print('1 1 1 1')
    else:
        print(*coords)