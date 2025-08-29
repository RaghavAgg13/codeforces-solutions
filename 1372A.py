for i in range(int(input())):
    n = int(input())
    for i in range(n//2):
        print(i*2+1, end=' ')
        print(i*2+1, end=' ')
    
    if n%2 == 1:
        print(n)
    else: print()