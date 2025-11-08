for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    c0,c1,c2 = 0,0,0
    for i in a:
        if i%3 == 0: c0 += 1
        elif i%3 == 1: c1 += 1
        else: c2 += 1
    
    # print(c0,c1,c2)

    avg = n//3
    ans = 0

    while not (c0 == c1 == c2):
        if c0 > avg:
            ans += c0 - avg
            c1 += c0 - avg
            c0 = avg
        if c1 > avg:
            ans += c1 - avg
            c2 += c1 - avg
            c1 = avg
        if c2 > avg:
            ans += c2 - avg
            c0 += c2 - avg
            c2 = avg
    
    # ans = abs(c0-avg)+abs(c1-avg)+abs(c2-avg)
    print(ans)