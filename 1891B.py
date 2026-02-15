for i in range(int(input())):
    n,q = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    x = [b[0]]
    for i in b:
        if i < x[-1]: x.append(i)
    
    # print(x)

    for i in range(n):
        for j in x:
            no = 2**j
            if not a[i]%no:
                a[i] += no//2
        print(a[i], end=' ')
    print()