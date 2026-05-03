for i in range(int(input())):
    n = int(input())

    a = [0]*(n*3)

    no = n+1
    for i in range(0, 3*n, 3):
        a[i] = i//3+1
        a[i+1] = no
        no += 1
        a[i+2] = no
        no += 1
    
    print(*a)