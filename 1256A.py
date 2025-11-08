for i in range(int(input())):
    a,b,n,s = list(map(int, input().split()))

    req_a = s//n

    if req_a <= a:
        if s%n <= b: print("YES")
        else: print('NO')
    else:
        if s%n + (req_a-a)*n <= b: print('YES')
        else: print('NO')