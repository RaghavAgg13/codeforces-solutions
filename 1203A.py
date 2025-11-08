for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    b = sorted(a)
    c = sorted(a, reverse=True)

    check = False
    for i in range(n):
        if a[i:]+a[:i] in [b,c]:
            check = True
            break
    
    print('YES' if check else "NO")

    