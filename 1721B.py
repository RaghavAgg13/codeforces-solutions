for i in range(int(input())):
    n,m,x,y,d = list(map(int, input().split()))

    start_blocked = abs(1 - x) + abs(1 - y) <= d
    end_blocked = abs(n - x) + abs(m - y) <= d

    if start_blocked or end_blocked:
        print(-1)
        continue

    vertical_wall = (x - d <= 1) and (x + d >= n)
    horizontal_wall = (y - d <= 1) and (y + d >= m)

    if vertical_wall or horizontal_wall:
        print(-1)
        continue

    print(n+m-2)