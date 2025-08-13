for i in range(int(input())):
    n = int(input())
    l = list(input())

    soln = []
    count = 0
    for i in l:
        if i == '#':
            if count >=3 :
                soln.append(count)
                break
            elif count != 0 : soln.append(count)
            count = 0
        else:
            count += 1
    if count != 0: soln.append(count)
    
    if len(soln) != 0:
        if max(soln) >=3: print(2)
        else: print(sum(soln))
    else: print(0)