n = int(input())


for i in range(n):
    soln = []
    a,b = list(map(int, input().split()))
    for i in range(a, b+1):
        soln.append(i-a + b-i)
    print(min(soln))