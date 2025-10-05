for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    check = 1
    for i in range(n-1):
        if a[i] == a[i+1] == -1:
            a[i] = 1
            a[i+1] = 1
            check = 0
            break
    
    final = sum(a)
    if check:
        if -1 not in a:
            final -= 4

    print(final)