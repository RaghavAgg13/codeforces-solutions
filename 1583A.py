import math
def checkComp(num):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return True
        
    return False
        

for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    start = sum(a)
    if checkComp(start):
        print(n)
        print(*[i+1 for i in range(n)])
    else:
        even_indices = []
        odd_incides = []

        for i in range(n):
            if not a[i]%2: even_indices.append(i+1)
            else: odd_incides.append(i+1)


        print(n-1)
        print(*even_indices , *odd_incides[:-1])