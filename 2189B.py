for _ in range(int(input())):
    n,x = list(map(int, input().split()))

    pair = []

    for i in range(n):
        a,b,c = list(map(int, input().split()))

        dist -= a*(b-1)
        pair.append(a*b-c)

    if (dist <= 0):
        print(0)
        continue
    
    if pair: pair.sort(reverse=True)

    max_gain = pair[0]

    if (max_gain <= 0):
        print(-1)
        continue

    cnt = (x+max_gain-1)//max_gain
    print(cnt)