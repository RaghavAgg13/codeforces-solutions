for i in range(int(input())):
    n = int(input())
    max = 0
    x = 0
    for i in range(2, n+1):
        for k in range(1, n//i+1):
            soln = i*k*(k+1)//2
            # print('for x =', i, 'k =', k, 'and the soln is:', soln)
            if soln > max:
                max = soln
                x = i
    print(x)