for i in range(int(input())):
    n = int(input())

    if n != 2:
        arr = []
        for i in range(1, n**2+1, 3): arr.append(i)
        for i in range(2, n**2+1, 3): arr.append(i)
        for i in range(3, n**2+1, 3): arr.append(i)
        if n == 3:
            print('2 9 7')
            print('4 6 3')
            print('1 8 5')
        else:
            for i in range(n): print(*arr[i*n: (i+1)*n])
    else: print(-1)