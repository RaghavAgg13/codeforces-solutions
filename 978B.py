n = int(input())
s = input()
soln = 0

count = 0
for i in s:
    if i == 'x': count += 1
    else:
        if count >= 3: soln += count-2
        count = 0

if count >= 3: soln += count-2

print(soln)