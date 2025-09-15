for i in range(int(input())):
    n = int(input())

    if n%2:
        for i in range(1, n//2+1):
            print(n+1-i, i, end=' ')
        print(n//2+1)

    else: print(-1)