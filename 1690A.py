for i in range(int(input())):
    n = int(input())

    if n%3 == 0:
        rem = 3
    else:
        rem = n%3+3

    b = int(n/3)
    if rem == 3:
        print(b,b+1,b-1)
    elif rem == 4:
        print(b,b+2,b-1)
    else:
        print(b+1,b+2,b-1)