for _ in range(int(input())):
    n,k,m = list(map(int, input().split()))

    if m < k:
        print("NO")
    else:
        print("YES")
        for i in range(n-1):
            print(1, end=' ')
        print(m-(k-1))