for i in range(int(input())):
    r,x,d,n = list(map(int, input().split()))
    types = input()

    cnt = 0
    for type in types:
        if r < x or type == '1':
            cnt += 1
            r -= d
            
    print(cnt)