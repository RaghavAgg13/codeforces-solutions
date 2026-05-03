for i in range(int(input())):
    n = int(input())
    nos = [([j for j in range(1, n*2+2)], 3)]
    ans = []

    chk = False

    while not chk:
        cur,t = nos.pop(0)
        if (t == 0):
            continue
        if (len(cur)) == t:
            ans.extend(cur)
            if len(ans) == 3:
                print("!", *ans)
                chk = True
            continue            
        
        odd = cur[:len(cur)//2]
        odd_set = set(odd)
        even = [x for x in range(1, n*2+2) if x not in odd_set]

        print("?", len(odd), *odd)
        a = int(input())
        print("?", len(even), *even)
        b = int(input())

        if a-b == 1:
            nos.append((odd, 1))
            nos.append((cur[len(cur)//2:], t-1))
        elif a - b == -1:
            nos.append((odd, 2))
            nos.append((cur[len(cur)//2:], t-2))
        elif (len(odd)-a)%2 != 0:
            nos.append((odd, 3))
            nos.append((cur[len(cur)//2:], 0))
        else:
            nos.append((odd, 0))
            nos.append((cur[len(cur)//2:], t))
