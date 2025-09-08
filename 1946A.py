for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    median = a[(n-1)//2]
    
    count = 0
    for i in range((n-1)// 2, n):
        if a[i] == median:
            count += 1
        else:
            break

    print(count)