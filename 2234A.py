for i in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())), reverse=True)

    for i in range(2, n):
        if a[i] != a[i-2]%a[i-1]:
            print(-1)
            break
    else:
        print(a[0], a[1])
    