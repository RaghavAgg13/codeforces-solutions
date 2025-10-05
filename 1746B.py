for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    count = 0
    if 1 in a and 0 in a:
        left, right = 0, n-1

        while left < right:
            while left < n and a[left] == 0:
                left += 1
            while right >= 0 and a[right] == 1:
                right -= 1

            if left < right:
                a[left], a[right] = 0, 1
                count += 1
                left += 1
                right -= 1
        
    print(count)