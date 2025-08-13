n,m = list(map(int, input().split(' ')))
peices = sorted(list(map(int, input().split(' '))))
a = max(peices) - min(peices)

for i in range(m-n+1):
    b = max(peices[i:n+i]) - min(peices[i:n+i])
    if a > b:
        a = b
print(a)