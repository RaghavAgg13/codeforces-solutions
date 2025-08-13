n = int(input())
l = list(map(int, input().split(' ')))

i1,i2,i3 = [],[],[]
count = 0
for i in l:
    if i == 1:
        i1.append(l[count:].index(i)+count)
    elif i == 2:
        i2.append(l[count:].index(i)+count)
    elif i == 3:
        i3.append(l[count:].index(i)+count)
    count += 1

s = min(len(i1), len(i2), len(i3))
print(s)

for j in range(s):
    print(1+i1[j], 1+i2[j], 1+i3[j])