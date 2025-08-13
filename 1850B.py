for i in range(int(input())):
    n = int(input())
    a = []
    b = []
    soln = []

    for i in range(n):
        ai, bi = list(map(int, input().split()))
        a.append(ai)
        b.append(bi)

    for i in range(n):
        if a[i]<= 10:
            soln.append(b[i])

    print(b.index(max(soln))+1)