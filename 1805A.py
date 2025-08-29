for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    xor = a[0]
    for i in range(1,n):
        xor ^= a[i]
    
    print(xor if n%2 or (not n%2 and xor == 0) else -1)