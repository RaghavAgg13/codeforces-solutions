from collections import Counter
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    b = sorted(Counter(a).items())
    
    start,sf = 0, b[0][1]
    check = True
    for i in range(len(b)):
        if b[i][0] == start:
            if not b[i][1]%sf:
                start, sf = b[i][0], b[i][1]
            else:
                check = False
                break
            start += 1
        else:
            start += 1
            check = False
            break
    
    if check:
        print(start)
    else:
        start = 0
        for i in set(a):
            if start == i:
                start += 1
            else:
                break
        
        print(start)