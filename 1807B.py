for i in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))

    score_m = 0
    score_b = 0
    for i in s:
        if i%2 == 0: score_m += i
        else: score_b += i


    if score_m > score_b: print('YES')
    else: print('NO')