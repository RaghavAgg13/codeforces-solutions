for i in range(int(input())):
    a = list(map(int, input().split()))

    c1 = a[0]+a[1]
    c2 = a[2]-a[1]
    c3 = a[3]-a[2]
    c = [c1, c2, c3]
    print(max(c.count(c1), c.count(c2), c.count(c3)))