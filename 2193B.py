for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    l = 0
    left = n
    while l < n:
        if a[l] == left:
            l += 1
            left -= 1
        else:
            break
            
    if l < n:
        r = a.index(left)
    else:
        l, r = 0, 0

    a = a[:l] + a[l: r+1][::-1] + a[r+1:]

    print(*a)