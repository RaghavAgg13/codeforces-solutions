for i in range(int(input())):
    n = int(input())
    a = []
    count = 0
    for i in range(n):
        c = input()
        if "*" in c:
            for j in range(n):
                if c[j] == '*': a.append([i+1, j+1])

    if a[0][0] == a[1][0]:
        if a[0][0] != 1:
            a.append([1, a[0][1]])
            a.append([1, a[1][1]])
        else:
            a.append([2, a[0][1]])
            a.append([2, a[1][1]])          
    elif a[0][1] == a[1][1]:
        if a[0][1] != 1:
            a.append([a[0][0], 1])
            a.append([a[1][0], 1])
        else:
            a.append([a[0][0], 2])
            a.append([a[1][0], 2])  
    else:
        a.append([a[0][0], a[1][1]])
        a.append([a[1][0], a[0][1]])
         
    for i in range(n):
        b = []
        for j in range(4): 
            if i+1 == a[j][0]: b.append(a[j][1]-1)

        c = ['.']*n
        for z in b: c[z] = "*"
        print(*c, sep="")