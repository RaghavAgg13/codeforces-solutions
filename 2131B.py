for i in range(int(input())):
    n = int(input())
    count_neg = 0
    for i in range(n):
        if not i%2:
            count_neg += 1
            print(-1, end=' ')
        elif i%2 and i == n-1:
            print(2, end=' ')
        else:
            print(3, end=' ')
    print()
