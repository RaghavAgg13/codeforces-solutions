n = int(input())
X, Y, Z = [], [], []
for i in range(n):
    x,y,z = list(map(int, input().split(" ")))
    X.append(x)
    Y.append(y)
    Z.append(z)
if sum(X) == sum(Y) == sum(Z) == 0:
    print('YES')
else:
    print('NO')
