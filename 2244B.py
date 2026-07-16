for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    s = 0
    sum = 0
    for i in range(n):
        s += i+1
        sum += a[i]

        if s > sum:
            print("NO")
            break
    else:
        print("YES")