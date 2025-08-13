for i in range(int(input())):
    n,a,b,c= list(map(int, input().split()))

    soln = 3*(n//(a+b+c))
    if n%(a+b+c) != 0 or n < a+b+c:
        rem = n%(a+b+c)
        if a+b < rem <a+b+c:
            soln += 3
        elif a < rem <= a+b:
            soln += 2
        else:
            soln += 1


    print(soln)