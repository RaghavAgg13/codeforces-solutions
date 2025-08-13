a,b,c,d = list(map(int, input().split()))
calories = 0
s = input()
for i in s:
    if i == '1':
        calories += a
    elif i == '2':
        calories += b
    elif i == '3':
        calories += c
    else: calories += d
print(calories)