for _ in range(int(input())):
    n = int(input())
    s = list(input())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))

    poss = True
    if s[0] == '1' and a[0] != c[0]:
        poss = False
    
    s[0] = '1'
    a[0] = c[0]

    cum_sum = a[0]
    prev = -1
    for i in range(1, n):
        if c[i] < c[i-1]:
            poss = False
            break

        if (s[i] == '0'): 
            prev = i
            a[i] = c[i]-cum_sum

        cum_sum += a[i]

        if cum_sum > c[i]:
            if prev == -1:
                poss = False
                break

            a[prev] -= cum_sum-c[i]
            cum_sum = c[i]

        if c[i] > c[i-1]:
            if cum_sum < c[i]:
                poss = False
            prev = -1

    if poss:
        print("YES")
        print(*a)
    else:
        print("NO")