for i in range(int(input())):
    n = int(input())

    for i in range(1, n//2):
        print(i*2, i*2-1, end=' ')
    if n%2 == 0:
        print(n, n-1)
    else:
        print(n, n-2, n-1)