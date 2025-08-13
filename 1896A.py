for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    b = False
    final = sorted(a)
    if final == a:
        b = True
    else:
        for i in range(n-2):
            for i in range(n-2, 0, -1):
                if a[i-1] < a[i] > a[i+1]:
                    a[i], a[i + 1] = a[i + 1], a[i]

        if final == a:
            b = True
            break
    
    print('YES' if b else 'NO')