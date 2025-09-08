for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    b = [n-a[i]+1 for i in range(n)]

    
    print(*b)