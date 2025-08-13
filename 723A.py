x1, x2, x3 = list(map(float, input().split(' ')))

a = int(min((abs(x1-x2) + abs(x1-x3)), (abs(x2-x1) + abs(x2-x3)), (abs(x3-x1) + abs(x3-x2))))
print(a)