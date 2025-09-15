for i in range(int(input())):
    n = int(input())
    a = list(map(str, input().split()))

    b = "".join(map(str, a))
    
    if '101' in b:
        print('NO')
    else: print('YES')