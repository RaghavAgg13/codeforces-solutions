for i in range(int(input())):
    x1,p1 = list(map(int, input().split()))
    x2,p2 = list(map(int, input().split()))

    p1,p2 = p1-min(p1,p2), p2-min(p1,p2)

    if p1 > 10:
        print(">")
        continue
    if p2 > 10:
        print("<")
        continue

    n1 = x1 * (10**p1)
    n2 = x2 * (10**p2)

    if (n1 > n2): print(">")
    elif (n1 < n2): print("<")
    else: print("=")