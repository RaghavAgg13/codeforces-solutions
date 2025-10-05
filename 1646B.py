for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    r,b,sr,sb = 0,1,0,a[0]
    left,right = 1, n-1

    found = False
    while left <= right:
        if sr > sb and r < b:
            found = True
            break

        sb += a[left]
        b += 1
        left += 1

        if left > right: break

        sr += a[right]
        r += 1
        right -= 1

    if sr > sb and r < b: found = True

    print("YES" if found else "NO")