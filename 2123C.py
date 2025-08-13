for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))

    nosmax = []
    nosmin = []
    for i in range(n):
            if max(l[:i+1]) not in nosmax: nosmax.append(max(l[:i+1]))
            if min(l[i:]) not in nosmin: nosmin.append(min(l[i:]))


    final = [nosmax[0]] + [nosmax[-1]] + [nosmin[0]] + [nosmin[-1]]

    soln = [0]*n
    for i in final:
          soln[l.index(i)] = 1
        
    for i in soln: print(i, end='')
    print()
