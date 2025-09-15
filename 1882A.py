for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    start = 0
    for i in range(n):
        if a[i] == i+1+start:
            start += 1

    print(start+n)