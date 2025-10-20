for i in range(int(input())):
    n,m = list(map(int, input().split()))

    matrix = []
    for i in range(n): 
        matrix.append(list(map(int, input().split())))

    if n == m == 1: 
        print(-1)
        continue

    if n != 1:
        for row in matrix[1:]: print(*row)
        print(*matrix[0])
    else:
        row = matrix[0]
        if not m%2:
            print(*row[::-1])
        else:
            print(*row[1:], row[0])