def cal(n):
    a = n
    sum = 0
    while n >= 10:
        sum += n%10
        n //= 10
    sum += n
    return sum

from math import ceil
n = int(input())

sum = 0
a = n
while a >= 10:
    sum += a%10
    a //= 10
sum += a

while sum%4:
    n += 1
    sum = 0
    a = n
    while a >= 10:
        sum += a%10
        a //= 10
    sum += a

print(n)