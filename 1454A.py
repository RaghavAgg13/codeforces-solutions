for i in range(int(input())):
    n = int(input())

    l = []
    for i in range(1, n+1):
        l.append(i)

    final = []
    for i in range(1, n+1):
        if i+1 in l:
            final.append(str(i+1))
        else:
            final.append(str(l[0]))
    
    print(' '.join(final))