for i in range(int(input())):
    n,m = list(map(int, input().split()))

    words = [input() for i in range(n)]

    soln = sum([abs(ord(words[0][k])-ord(words[1][k])) for k in range(m)])
    for i in range(n-1):
        for j in range(i+1, n):
            alpha = sum([abs(ord(words[i][k])-ord(words[j][k])) for k in range(m)])
            soln = min(alpha, soln)

            if not soln: break
    
    print(soln)