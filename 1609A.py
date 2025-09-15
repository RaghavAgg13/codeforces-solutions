for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    count = 1
    for i in range(n):
        while not a[i]%2:
            count *= 2
            a[i] //= 2

    print(sum(a)-max(a)+max(a)*count)