for i in range(int(input())):
    n,k = list(map(int, input().split()))
    a = [input() for i in range(n)]

    for i in range(0, n, k):
        print(''.join(a[i][j] for j in range(0, n, k)))