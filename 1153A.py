from math import ceil
n,t = list(map(int, input().split()))

bus = []
for i in range(n):
    x,y = list(map(int, input().split()))
    if x >= t: 
        bus.append((x,y, i+1))
    else:
        start = x + ceil((t-x)/y)*y
        bus.append((start,y,i+1))

bus.sort(key=lambda item:item[0])

min = bus[0][0]
m = []
for i in bus:
    if i[0] == min:
        m.append(i)
    else: break

m.sort(key=lambda item:item[1])

# print(m)
print(m[0][2])