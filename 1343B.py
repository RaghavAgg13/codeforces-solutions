t = int(input())

for i in range(t):
    n = int(int(input())/2)
    if n%2 != 0:
        print('NO')
    else:
        print('YES')
        for i in range(1, n+1):
            print(i*2, end=' ')
        for i in range(1, int(n/2)+1):
            print(i*2-1, end=' ')
        for i in range(int(n/2) + 1, n+1):
            print(i*2+1, end=' ')
        print()
