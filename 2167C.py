for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    even,odd = [],[]
    for i in a:
        if i%2: odd.append(i)
        else: even.append(i)


    if even != [] and odd != []:
        even.sort()
        odd.sort()
        ti, tj= len(even), len(odd)
        i,j = 0,0
        while i < ti and j < tj:
            if even[i] < odd[j]:
                print(even[i], end=' ')
                i += 1
            else:
                print(odd[j], end=' ')
                j += 1
        
        while i < ti:
            print(even[i], end=' ')
            i += 1
        while j < tj:
            print(odd[j], end=' ')
            j += 1
        
        print()
    else:
        print(*even, *odd)