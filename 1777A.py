for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    count = 0
    for i in range(n-1):
        if a[i]%2 == a[i+1]%2:
            count += 1
    
    print(count)