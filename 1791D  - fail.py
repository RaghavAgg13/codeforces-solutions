for i in range(int(input())):
    n = int(input())
    a = list(input())

    total = len(set(a))
    soln = (len(set(a[0]))+len(set(a[1:])))

    if total == 1:
        soln = 2
    elif n == total:
        soln = total
    elif soln < total*2:
        for i in range(2, n):
            if len(set(a[:i]))+len(set(a[i:])) >= soln: soln = len(set(a[:i]))+len(set(a[i:]))
            else: break

            if soln >= total*2: break

    print(soln)