for i in range(int(input())):
    a,b,n = list(map(int, input().split()))
    w = sorted(list(map(int, input().split())))

    time = b-1
    b = 1
    while b > 0:
        
        if w != []:
            b = min(b+w[0], a)
            w.remove(w[0])

        if b > 1:
            time += b-1
            b = 1
        else: b = 0

    print(time+1)