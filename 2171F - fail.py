for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    m = n
    for i in range(n-1):
        m = min(m, a[i])
        if m == n-i: 
            print('NO')
            break
    else:
        print("YES")
        seen = set()
        for i in range(n-1):
            for j in range(i+1, n):
                if a[j]>a[i] and not (a[i] in seen and a[j] in seen):
                    print(a[j],a[i])
                    seen.add(a[i])
                    seen.add(a[j])
