n = int(input())
a = input()

divisors = []
for i in range(2, n+1):
    if not n%i: divisors.append(i)

for i in divisors:
    a = a[:i][::-1] + a[i:]

print(*a, sep = '')