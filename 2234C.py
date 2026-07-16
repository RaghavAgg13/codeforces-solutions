for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n):
        cost = 0
        l,r = (i-1)%n, i
        l_max, r_max = a[l], a[r]

        for _ in range(n-1):
            if l_max <= r_max:
                cost += l_max
                l = (l-1)%n
                l_max = max(l_max, a[l])
            else:
                cost += r_max
                r = (r+1)%n
                r_max = max(r_max, a[r])
        
        print(cost, end=" ")
    print()