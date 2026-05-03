for i in range(int(input())):
    n,m = list(map(int, input().split()))
    a = list(map(str, input().split()))
    b = ''.join(a[n-m:])
    
    chk = 0
    if (m <= n):
        count = 1
        for j in range(1, n):
            if a[j] == a[j-1]:
                count += 1
                if count >= m:
                    chk = 1
                    print("NO")
                    break
            else:
                count = 1
    
    if chk:
        continue

    t = 0
    pos = 0
    while pos != n:
        if (int(a[pos])+t)%m != 0:
            pos += 1
        
        t += 1
    
    print("YES")
# else:
#     print("NO")