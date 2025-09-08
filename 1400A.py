for i in range(int(input())):
    n = int(input())
    a = input()

    s = ''
    for i in range(n):
        s += a[i:n+i+1][i]

    print(s)