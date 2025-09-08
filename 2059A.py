for i in range(int(input())):
    n = int(input())
    
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    d = len(set(a))+len(set(b))-1
    print('YES' if d >= 3 else 'NO')