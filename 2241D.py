for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a += [0]

    for i in range(n):
        if a[i] > b[i]:
            print("NO")
            break
        elif a[i] < b[i]:
            a[i+1] -= b[i]-a[i]
            a[i] += b[i]-a[i]
    else:
        print("YES")
