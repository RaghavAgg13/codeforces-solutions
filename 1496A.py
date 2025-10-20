for i in range(int(input())):
    n,k = list(map(int, input().split()))
    a = input()

    left,right = 0, n-1
    while left < right:
        if a[left] == a[right]:
            left += 1
            right -= 1
        else:
            break
        
        if left >= k: break

    if left >= k:
        print('NO' if left-1==right and left == k else 'YES')
    else:
        print('NO')