for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    check = True
    a.sort()
    for i in range(1, n, 2):
        if i+1 < n and a[i] != a[i+1]:
            check = False
            break
    
    print("YES" if check else "NO")