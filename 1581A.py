from math import factorial
for i in range(int(input())):
    n = int(input())

    print((factorial(2*n)//2)%1000000007)