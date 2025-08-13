for i in range(int(input())):
    n,m = list(map(int, input().split()))

    if n%2 == m%2 == 0:
        soln = n*m//2
    elif n%2 == m%2 == 1:
        rem = n+m-1
        soln = (n-1)*(m-1)//2 + rem//2
        if rem%2 == 1: soln += 1

    elif (n%2 == 0 and m%2 == 1):
        soln = n*(m-1)//2 + n//2
    else:
        soln = (n-1)*m//2 + m//2

    print(soln)