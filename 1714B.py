for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    seen = set()
    length = 0
    
    for i in range(n - 1, -1, -1):
        if a[i] in seen:
            length = i + 1
            break
        
        seen.add(a[i])
        
    print(length)