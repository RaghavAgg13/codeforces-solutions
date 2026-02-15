a = []

n = int(input())
for i in range(n):
    repo = list(map(int, input().split()))
    a.append(repo)

for i in range(n-1):
    for j in range(i+1, n):
        if a[i] != [] and a[j] != []:
            if a[i][0] > a[j][0] and a[i][1] > a[j][1] and a[i][2] > a[j][2] and a[i][3] > a[j][3]:
                a[j] = []
            elif  a[i][0] < a[j][0] and a[i][1] < a[j][1] and a[i][2] < a[j][2] and a[i][3] < a[j][3]:
                a[i] = []

idx = 0
price = 1001
for i in range(n):
    if a[i] != [] and a[i][3] < price:
        idx = i+1
        price = a[i][3]

print(idx)