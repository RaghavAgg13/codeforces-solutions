for i in range(int(input())):
    n = int(input())

    cur = 2
    print(cur, end=' ')
    for i in range(n-1):
        cur = cur+1
        print(cur, end=' ')
    print()