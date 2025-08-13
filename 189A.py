l = list(map(int, input().split(' ')))
n = l[0]
a,b,c = sorted(l[1:])
soln = [0]
y = False

# if n//a > 3:
#     x = n//a - 3
# else:
#     x = 1
# n -= x * a

# for k in range(n//a + 1):
#     for j in range(n//b + 1):
#         for i in range(n//c + 1):
#             if n == (c * i) + (b * j) + (a * k):
#                 soln.append(i+j+k)
#                 break

# if soln == [0]: y = True
# if soln == [0] and n % c == 0:
#     y = False
#     x = n // c

# while y:
#     n += x * a
#     x = 0
#     soln = [0]
#     for k in range(n//a + 1):
#         for j in range(n//b + 1):
#             for i in range(n//c + 1):
#                 if n == (c * i) + (b * j) + (a * k):
#                     soln.append(i+j+k)
#                     y = False

if n//a > 3:
    x = n//a - 3
else:
    x = 1
n -= x * a

for i in range(n // a + 1):
    for j in range((n - a * i) // b + 1):
        rem = n - a * i - b * j
        if rem % c == 0:
            k = rem // c
            soln.append(i + j + k) 

if soln == [0]: y = True
while y == True:
    n += x * a
    x = 0

    for i in range(n // a + 1):
        for j in range((n - a * i) // b + 1):
            rem = n - a * i - b * j
            if rem % c == 0:
                k = rem // c
                soln.append(i + j + k)
                y = False

print(max(soln) + x)