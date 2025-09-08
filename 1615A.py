for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    s = sum(a)

    if not s%n: print(0)
    else: print(1)