for i in range(int(input())):
    n,k = list(map(int, input().split()))

    if k <= n//2+n%2:
        grid = [['.' for i in range(n)] for i in range(n)]
        for i in range(k):
            grid[i*2][i*2] = 'R'
        
        for row in grid:
            print(*row, sep='')
        
    else:
        print(-1)