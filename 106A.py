s = input()
a,b = list(map(str, input().split()))

x, y = [], []
x.append(a[1])
y.append(b[1])

for i in [a,b]:
    if i[0] == 'T': z = 10
    elif i[0] == "J": z = 11
    elif i[0] == "Q": z = 12
    elif i[0] == "K": z = 13
    elif i[0] == "A": z = 14
    else: z = int(i[0])

    if i == a: x.append(z)
    else: y.append(z)

# print(x,y)

if x[0] == y[0]:
    print("YES" if x[1] > y[1] else "NO")
elif x[0] == s:
    print("YES")
else: print("NO")