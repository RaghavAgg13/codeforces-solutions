for i in range(int(input())):
    n,a,b = list(map(int, input().split()))

    left = [a]
    right = [b]
    if (a <= n//2 and b >= n//2+1) or (a == n//2+1 and b == n//2):
        for i in range(n, 0, -1):
            if i != a and i != b:
                if len(left) < n//2:
                    left.append(i)
                else:
                    right.append(i)

        print(*left, *right)

    else:
        print(-1)