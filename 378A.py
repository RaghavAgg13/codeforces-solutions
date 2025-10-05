a,b = list(map(int, input().split()))

c = [0]*3
for i in range(1, 7):
    x,y = abs(a-i), abs(b-i)
    if x > y: c[2] += 1
    elif x < y: c[0] += 1
    else: c[1] += 1

print(*c) 