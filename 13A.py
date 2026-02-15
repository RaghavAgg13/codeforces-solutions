from math import gcd
a = int(input())

sum = 0
for i in range(2, a):
    t = a
    while t >= i:
        sum += t%i
        t //= i
    sum += t
    
b = gcd(sum, a-2)
print(sum//b, '/', (a-2)//b, sep='')