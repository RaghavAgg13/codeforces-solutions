for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    count = 0
    for i in range(n):
        count = max(count, a[i]-i-1)
    
    print(count)