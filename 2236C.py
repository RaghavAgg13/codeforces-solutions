for i in range(int(input())):
    a,b,x = list(map(int, input().split()))

    if a > b: a,b = b,a

    ans = float('inf')
    ta,steps_a = a,0
    while True:
        tb, steps_b = b,0
        while True:
            moves = steps_a+steps_b + abs(ta-tb)
            ans = min(ans, moves)

            if tb == 0: break
            tb //= x
            steps_b += 1
    
        if ta == 0: break
        ta //= x
        steps_a += 1

    print(ans)