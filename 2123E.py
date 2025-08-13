import math
for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))

    def findMex(l):
        mex = 0
        while True:
            if mex not in l:
                return mex
            mex += 1

    mex = findMex(l)
    soln = [1]
    n1 = len(list(set(l)))
    for i in range(2, n+1):
        mex = (math.factorial(n) // (math.factorial(i) * math.factorial(n - i))) - math.factorial(n1) // (math.factorial(i) * math.factorial(n1 - i)) - (n-n1)
        soln.append(mex)
        print(mex)
    print(soln)