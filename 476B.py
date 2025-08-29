from math import factorial
s1 = input()
s2 = input()

d1 = s1.count('+')-s1.count('-')
d2 = s2.count('+')-s2.count('-')
delta = s2.count("?")

if delta >= abs(d1-d2):
    sum = 0
    for i in range(delta+1):
        if (delta-i) == abs(d1-d2):
            sum += ((0.5)**delta)*factorial(delta)/factorial(i//2)/factorial(delta-i//2)
    print(sum)
else:
    print(0)