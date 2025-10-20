for i in range(int(input())):
    n = int(input())

    for i in range(1, n//2+1):
        print(i, n-i+1, end=' ')
    if n%2:
        print(n//2+1)
    else: print()