for i in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    if n == 1:
        print(a[0] + x)
    else:
        def check(mid):
            return sum(max(0, mid - val) for val in a)

        left, right = min(a), max(a) + x
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if check(mid) <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        print(ans)