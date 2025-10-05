for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    count = 0
    splits = 0
    for i in range(n):
        if a[i]:
            count += 1
        else:
            if count: splits += 1
            count = 0
    
    if count: splits += 1
    print(splits if splits <= 2 else 2)