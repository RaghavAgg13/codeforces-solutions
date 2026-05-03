for i in range(int(input())):
    a,b = sorted(list(map(int, input().split())))
    c,d = a,b

    step = 1
    no = b
    layers = 0
    while (no >= step):
        layers += 1
        if (no == a):
            a -= step
            no = b
        else:
            b -= step
            no = a
        step *= 2
        
    layers_ = 0
    no = c
    step = 1
    while (no >= step):
        layers_ += 1
        if (no == c):
            c -= step
            no = d
        else:
            d -= step
            no = c
        step *= 2
    
    print(max(layers, layers_))
        
    