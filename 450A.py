n,m = list(map(int, input().split()))
beta = list(map(int, input().split()))
req = [[beta[i], i+1] for i in range(n)]

i = 0
while len(req) != 1:
    if req[0][0] > m:
        req[0][0] -= m
        a = req[0]
        req.remove(a)
        req.insert(len(req), a)
    else:
        req.remove(req[i])

print(req[0][1])