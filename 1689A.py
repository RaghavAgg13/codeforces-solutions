for i in range(int(input())):
    n,m,k = list(map(int, input().split()))
    c = ''

    a = ''.join(sorted(input()))
    b = ''.join(sorted(input()))

    l1, l2 = 0,0
    count, prev = 0, 1 if a[l1] < b[l1] else 0
 
    while l1 < n and l2 < m:
        if (a[l1] < b[l2] and (prev != 1 or count < k)) or (prev == 0 and count == k):
            c += a[l1]
            l1 += 1
            if prev == 1:
                count += 1
            else:
                prev, count = 1, 1
        else:
            c += b[l2]
            l2 += 1
            if prev == 0:
                count += 1
            else:
                prev, count = 0, 1
    
    print(c)