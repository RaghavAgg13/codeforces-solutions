for i in range(int(input())):
    n = int(input())
    
    soln = n//10
    if n%10 == 9: soln += 1
    print(soln)
    