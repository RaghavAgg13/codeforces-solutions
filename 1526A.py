for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    left,right = 0,2*n-1
    while left < right:
        if left < n: 
            print(a[left], end=' ')
            left += 1
        if right > -1:
            print(a[right], end=' ')
            right -= 1
    print()