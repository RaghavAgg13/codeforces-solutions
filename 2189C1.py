for i in range(int(input())):
    n = int(input())

    a = [0]*(n+1)
    for i in range((n+1)//2):
        no = i+1
        a[no] = no^1
        no2 = n-no+1
        a[no2] = no2^1
        
        if no == 1:
            a[1] = n - n%2
            a[n] = 1

    print(*a[1:])