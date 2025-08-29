for i in range(int(input())):
    n,m = list(map(int, input().split()))

    count = 0
    c = 0
    b = True
    for i in range(n):
        a = input()
        if count <= m and b:
            if count + len(a) <= m:
                count += len(a)
                c += 1
            else: b = False
        else:
            b = False
    
    print(c)