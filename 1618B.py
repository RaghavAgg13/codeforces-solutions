for i in range(int(input())):
    n = int(input())
    a = list(map(str, input().split()))

    b = a[0][0]
    check = False
    for i in range(n-3):
        if a[i][-1] == a[i+1][0]:
            b += a[i][-1]
        else:
            b += a[i][-1]
            b += a[i+1][0]
            check = True
    
    print(b+a[-1][-1] if check else b+a[-1][-1]*2)