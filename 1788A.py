for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))

    soln = -1
    twos = 0
    total = l.count(2)

    for x in range(n):
        i = l[x]
        if i == 2: twos += 1

        if twos*2 == total:
            soln = x+1
            break

    print(soln)