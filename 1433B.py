for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    start = a.index(1)
    sum = 0
    for i in range(start+1, n):
        if a[i] == 1:
            sum += i-start-1
            start = i

    print(sum)