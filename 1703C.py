for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        no, b = list(map(str, input().split()))
        for move in b:
            a[i] += 1 if move == 'D' else -1
            if a[i] > 9: a[i]-=10
            elif a[i] < 0: a[i]+=10

    print(*a)