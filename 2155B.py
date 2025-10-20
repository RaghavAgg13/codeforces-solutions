for i in range(int(input())):
    n,k = list(map(int, input().split()))

    if k == n*n-1:
        print('NO')
    else:
        print('YES')
        for i in range(1, k+1):
            print("U", end='')
            if not i%(n): print()
        
        if k != n*n:
            start_row, start_column = k//n,k%n
            if start_row == n-1:
                print('RL'*((n-start_column)//2), 'L'*((n-start_column)%2), sep='')
            else:
                print('D'*(n-start_column), sep='')
            for i in range(start_row+1, n):
                print('RL'*(n//2), 'L'*(n%2), sep='')