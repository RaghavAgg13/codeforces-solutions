for i in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))

    if n == 1:
        print(0)
    else:
        print(sum(a[n//2+bool(n%2):n])-sum(a[:n//2]))