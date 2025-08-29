
for i in range(int(input())):
    n = int(input())
 
    if n%3 == 0:
        print(n//3)
    elif n%2 == 0:
        if n>4:
            print(min(n//2, n//3+1))
        else:
            print(min(n//2, n//3+2))
    else:
        if n>4:
            print(n//3+1)
        else:
            print(n//3+2)