n, t = list(map(int,input().split(' ')))
a = input()
order = []
f1 = ''
for i in range(n):
    order.append(a[i])

for i in range(t):
    todo = []
    for j in range(0, n-1):
        if order[j] == 'B' and order[j+1] == 'G':
            todo.append(j)
        
    for a in todo:
        order[a] = 'G'
        order[a+1] = 'B'


for i in order:
    f1 += i
print(f1)