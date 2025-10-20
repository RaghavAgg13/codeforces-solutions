for i in range(int(input())):
    a,b,c,d = list(map(int, input().split()))
    ans = 0

    for i in range(a,b+1):
        if c <= i <= d:
            ans = i
            break
    if not ans: ans = a+c
    print(ans)