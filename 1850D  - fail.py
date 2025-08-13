for i in range(int(input())):
    n,k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    l1 = list(sorted(a, reverse=True))
    l2 = list(sorted(a))
    l3 = l1.copy()

    count1 = 0
    i = 1
    while i <= n-1-count1:
        if l1[i-1] - l1[i] > k:
            l1.remove(l1[i])
            count1 += 1
            i -= 1
        i += 1

    count2 = 0
    i = 1
    while i <= n-1-count2:
        if l2[i] - l2[i-1] > k:
            l2.remove(l2[i])
            count2 += 1
            i -= 1
        i += 1



    print(min(count1, count2    ))